import os
import random
import sys
import time

import dgl
import numpy as np
import tqdm

num_walks_per_node = 1000
walk_length = 100
path = sys.argv[1]


def construct_graph():
    formal_language_ids = []
    formal_language_names = []
    paper_ids = []
    paper_names = []
    application_ids = []
    application_names = []
    f_3 = open(os.path.join(path, "id_paper.txt"), encoding="ISO-8859-1")
    f_4 = open(os.path.join(path, "id_application.txt"), encoding="ISO-8859-1")
    f_5 = open(os.path.join(path, "formal_language.txt"), encoding="ISO-8859-1")
    while True:
        z = f_3.readline()
        if not z:
            break
        z = z.strip().split()
        identity = int(z[0])
        paper_ids.append(identity)
        paper_names.append(z[1])
    while True:
        w = f_4.readline()
        if not w:
            break
        w = w.strip().split()
        identity = int(w[0])
        application_ids.append(identity)
        application_names.append(w[1])
    while True:
        v = f_5.readline()
        if not v:
            break
        v = v.strip().split()
        identity = int(v[0])
        formal_language_name = "p" + "".join(v[1:])
        formal_language_ids.append(identity)
        formal_language_names.append(formal_language_name)
    f_3.close()
    f_4.close()
    f_5.close()

    paper_ids_invmap = {x: i for i, x in enumerate(paper_ids)}
    application_ids_invmap = {x: i for i, x in enumerate(application_ids)}
    formal_language_ids_invmap = {x: i for i, x in enumerate(formal_language_ids)}

    formal_language_paper_src = []
    formal_language_paper_dst = []
    formal_language_application_src = []
    formal_language_application_dst = []
    f_1 = open(os.path.join(path, "formal_language_paper.txt"), "r")
    f_2 = open(os.path.join(path, "formal_language_application.txt"), "r")
    for x in f_1:
        x = x.split("\t")
        x[0] = int(x[0])
        x[1] = int(x[1].strip("\n"))
        formal_language_paper_src.append(formal_language_ids_invmap[x[0]])
        formal_language_paper_dst.append(paper_ids_invmap[x[1]])
    for y in f_2:
        y = y.split("\t")
        y[0] = int(y[0])
        y[1] = int(y[1].strip("\n"))
        formal_language_application_src.append(formal_language_ids_invmap[y[0]])
        formal_language_application_dst.append(application_ids_invmap[y[1]])
    f_1.close()
    f_2.close()

    hg = dgl.heterograph(
        {
            ("formal_language", "pa", "paper"): (formal_language_paper_src, formal_language_paper_dst),
            ("paper", "ap", "formal_language"): (formal_language_paper_dst, formal_language_paper_src),
            ("formal_language", "pc", "application"): (formal_language_application_src, formal_language_application_dst),
            ("application", "cp", "formal_language"): (formal_language_application_dst, formal_language_application_src),
        }
    )
    return hg, paper_names, application_names, formal_language_names


# "applicationerence - formal_language - paper - formal_language - applicationerence" metapath sampling
def generate_metapath():
    output_path = open(os.path.join(path, "output_path.txt"), "w")
    count = 0

    hg, paper_names, application_names, formal_language_names = construct_graph()

    for application_idx in tqdm.trange(hg.num_nodes("application")):
        traces, _ = dgl.sampling.random_walk(
            hg,
            [application_idx] * num_walks_per_node,
            metapath=["cp", "pa", "ap", "pc"] * walk_length,
        )
        for tr in traces:
            outline = " ".join(
                (application_names if i % 4 == 0 else paper_names)[tr[i]]
                for i in range(0, len(tr), 2)
            )  # skip formal_language
            print(outline, file=output_path)
    output_path.close()


if __name__ == "__main__":
    generate_metapath()