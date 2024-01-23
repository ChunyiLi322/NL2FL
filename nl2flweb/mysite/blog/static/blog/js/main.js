jQuery(function ($) {
  "use strict";
  $("li.dropdown")
    .find(".fa-angle-down")
    .each(function () {
      $(this).on("click", function () {
        if ($(window).width() < 768) {
          $(this).parent().next().slideToggle();
        }
        return false;
      });
    });
  if ($("#video-container").length) {
    $("#video-container").fitVids();
  }
  new WOW().init();
  $(window).load(function () {
    $(".main-slider").addClass("animate-in");
    $(".preloader").remove();
    if ($(".masonery_area").length) {
      $(".masonery_area").masonry();
    }
    var $portfolio_selectors = $(".portfolio-filter >li>a");
    if ($portfolio_selectors.length) {
      var $portfolio = $(".portfolio-items");
      $portfolio.isotope({
        itemSelector: ".portfolio-item",
        layoutMode: "fitRows"
      });
      $portfolio_selectors.on("click", function () {
        $portfolio_selectors.removeClass("active");
        $(this).addClass("active");
        var selector = $(this).attr("data-filter");
        $portfolio.isotope({ filter: selector });
        return false;
      });
    }
  });
  $(".timer").each(count);
  function count(options) {
    var $this = $(this);
    options = $.extend({}, options || {}, $this.data("countToOptions") || {});
    $this.countTo(options);
  }
  $(".fa-search").on("click", function () {
    $(".field-toggle").fadeToggle(200);
  });
  var form = $("#main-contact-form");
  form.submit(function (event) {
    event.preventDefault();
    var form_status = $('<div class="form_status"></div>');
    $.ajax({
      url: $(this).attr("action"),
      beforeSend: function () {
        form.prepend(
          form_status
            .html(
              '<p><i class="fa fa-spinner fa-spin"></i> Email is sending...</p>'
            )
            .fadeIn()
        );
      }
    }).done(function (data) {
      form_status
        .html(
          '<p class="text-success">Thank you for contact us. As early as possible  we will contact you</p>'
        )
        .delay(3000)
        .fadeOut();
    });
  });
  $.each($("div.progress-bar"), function () {
    $(this).css("width", $(this).attr("data-transition") + "%");
  });
  if ($("#gmap").length) {
    var map;
    map = new GMaps({
      el: "#gmap",
      lat: 43.04446,
      lng: -76.130791,
      scrollwheel: false,
      zoom: 16,
      zoomControl: false,
      panControl: false,
      streetViewControl: false,
      mapTypeControl: false,
      overviewMapControl: false,
      clickable: false
    });
    map.addMarker({
      lat: 43.04446,
      lng: -76.130791,
      animation: google.maps.Animation.DROP,
      verticalAlign: "bottom",
      horizontalAlign: "center",
      backgroundColor: "#3e8bff"
    });
  }
});

function selectOnchang(obj){
 var value = obj.options[obj.selectedIndex].value;
 alert(value);
}


//11-10 增加loading功能
function loadingEffect() {
    var loading = $('#fountainG');
    loading.hide();
    $(document).ajaxStart(function () {
        loading.show();
    }).ajaxStop(function () {
        loading.hide();
    });
}
loadingEffect();



$.ajaxSetup({
            beforeSend: function () {
             document.getElementById('loading').style.display = 'block';
                //ajax请求之前
            },
            complete: function () {
              document.getElementById('loading').style.display = 'none';
                //ajax请求完成，不管成功失败
            },
            error: function () {
              alert("网络不通");
            }
});

//——————————————————————————————————————————————————————————————————————————————————————————————
function postnl(obj){
 alert("测试button action");
}

 $(function (){
    $('#nl2flsubmit').click(function(){
      let flcheckboxlist = []
　　　　$("input[name='flcheckbox']:checked").each(function(){
         flcheckboxlist.push($(this).attr("data-labelauty"))
　　　　});
      let flpracheckboxlist = []
　　　　$("input[name='flpracheckbox']:checked").each(function(){
         // alert($(this).attr("data-labelauty"))
         flpracheckboxlist.push($(this).attr("data-labelauty"))
　　　　});
     $.ajax({
     'url':'/postnl/',  //访问的url地址
     'dateType':'json',  //想要获得的返回数据类型
     type:'post',
     data:{
       ChatGptAPIname:$('#ChatGptAPIname').val(),
       nlmessage:$('#nlmessage').val(),
       ChatGptversion:$('#ChatGptversion').val(),
       flcheckbox:JSON.stringify(flcheckboxlist),
       flpracheckbox:JSON.stringify(flpracheckboxlist),
       csrfmiddlewaretoken:$('[name=csrfmiddlewaretoken]').val(),
     }
     }).success(function(res){  //执行成功的回调函数（含有返回的数据（date））
       console.log(res)
       var res_Str = JSON.parse(res);
       console.log(res_Str,typeof res_Str);
       $('#flmessage').val(res_Str['flmessage'])
       $('#flpramessage').val(res_Str['flpramessage'])
     })
    })
 })

// $('#nl2flsubmit').click(function () {
//     var loading = $('#fountainG');
//     loading.show();
//     $.when(getAjaxData()).done(function (res) {
//         loading.hide();
//         console.log(res)
//     });
// })



 $(function(){
    $('#fl2img').click(function(){

     $.ajax({
     'url':'/postflimg/',  //访问的url地址
     'dateType':'json',  //想要获得的返回数据类型
     type:'post',
     data:{
       flmessage:$('#flmessage').val(),
       flpramessage:$('#flpramessage').val(),
       csrfmiddlewaretoken:$('[name=csrfmiddlewaretoken]').val(),
     }
     }).success(function(res){  //执行成功的回调函数（含有返回的数据（date））
       alert("已成功生成")
       console.log(res)
       var res_Str = JSON.parse(res);
       console.log(res_Str,typeof res_Str);
       $('#pathdir').attr("src",res_Str['pathdir']+ "?" + Math.random())
       // $('#pathdir').src.val(res_Str['pathdir'])
     })
    })
 })




// $("#fl2img").click(function(){
// 　　alert("Hello World  click");
//  });



//11-15 增加网站上传功能
function uploadFile() {
    // 获取表单数据
    var form_data = new FormData();
    var file_info = $('#file')[0];
    console.log(file_info)
    form_data.append('file', file_info.files[0]);
    form_data.append('text1', $("#filepageone").val());
    form_data.append('text2', $("#filepagetwo").val());
    console.log(form_data)
    $.ajax({
        'url': "/filesolve/",
        // 'dateType':'json',
        type: "post",
        contentType: false,
        processData: false,
        data: form_data,
        success: function (data) {
            // 显示上传成功的信息
            var textlist = JSON.parse(data);
            var list = textlist['text_list']
            // alert(textlist['text_list'])
            console.log("----------------------",textlist['text_list'])

            var div = document.getElementById("textcontainer");
            div.innerHTML = "";
            var div2 = document.getElementById("textcontainerbutton");
            div2.innerHTML = "";

            $("#filemessage").text("文件上传成功");
            alert("进入list1")
            for (var i = 0; i < list.length; i++) {
              alert("进入list")
              // 创建一个 input 元素
              var input = $("<input>");
              // 设置 input 的类型为 checkbox 或 radio，根据你的需要修改
              input.attr("type", "checkbox");
              // 设置 input 的 name 属性，根据你的需要修改
              input.attr("name", "textcheckbox");
              input.attr("class", "labelautybg2");
              // 设置 input 的 value 属性为列表的对应值
              input.attr("value", list[i]);
              // 设置 input 的 data-labelauty 属性为列表的对应值，这会显示在 labelauty 的样式中
              input.attr("data-labelauty", list[i]);
              // 追加 input 到 div 元素中
              $("#textcontainer").append(input);
            }
            // 调用 labelauty 的方法
            $("#textcontainer input").labelauty();

            // 创建一个 input 元素
            var input2 = $("<input>");
            // 设置 input 的类型为 checkbox 或 radio，根据你的需要修改
            input2.attr("type", "button");
            // 设置 input 的 name 属性，根据你的需要修改
            input2.attr("id", "simcompute");
            input2.attr("class", "btn btn-submit");
            // 设置 input 的 value 属性为列表的对应值
            input2.attr("value", "相关性评估");
            // 设置 input 的 data-labelauty 属性为列表的对应值，这会显示在 labelauty 的样式中
            input2.attr("style", "width: 40%");
            // 追加 input 到 div 元素中
            $("#textcontainerbutton").append(input2);
        },
        error: function (data) {
            // 显示上传失败的信息
            $("#filemessage").text("需求提取失败");

        }
     })
}





//——————————————————————————————————————————————————————————————————————————————————————————————
//11-21 相似性计算的功能

 $(function (){
    $('#textcontainerbutton').click(function(){
      let textcheckboxlist2 = []
　　　　$("input[name='textcheckbox']:checked").each(function(){
         textcheckboxlist2.push($(this).attr("data-labelauty"))
　　　　});
     $.ajax({
     'url':'/computesim/',  //访问的url地址
     'dateType':'json',  //想要获得的返回数据类型
     type:'post',
     data:{
       textcheckbox:JSON.stringify(textcheckboxlist2),
       csrfmiddlewaretoken:$('[name=csrfmiddlewaretoken]').val(),
     }
     }).success(function(res){  //执行成功的回调函数（含有返回的数据（date））
       console.log(res)
       var res_Str = JSON.parse(res);
       console.log(res_Str,typeof res_Str);
       $('#nlmessage').val(res_Str['nlmessage'])

        var div3 = document.getElementById("simloading");
        div3.innerHTML = "";


       // 创建一个div元素，用来显示进度条
        var progressDiv = $("<div></div>");
        // 设置div的样式，包括宽度、高度、边框、背景色等
        progressDiv.css({
          width: "300px",
          height: "20px",
          border: "1px solid black",
          backgroundColor: "white"
        });
        // 将div添加到页面中
        $("#simloading").append(progressDiv);


        // 定义一个函数，用来根据相似度更新进度条和进度值
        function updateProgress(similarity) {
          // 将相似度转换为百分比，并保留两位小数
          var percentage = (similarity * 100).toFixed(2) + "%";
          // 设置span的文本为百分比
          progressSpan.text(percentage);
          // 设置div的背景色渐变，根据相似度的大小显示不同的颜色
          // 参考：[CSS3 渐变（Gradient）](https://www.cnblogs.com/qianzf/p/7074211.html)
          progressDiv.css({
            background: "linear-gradient(to right, gray " + percentage + ", white " + percentage + ")"
          });
        }


        // 创建一个span元素，用来显示进度值
        var progressSpan = $("<span></span>");
        // 设置span的样式，包括字体大小、颜色、位置等
        progressSpan.css({
          fontSize: "18px",
          color: "white",
          position: "absolute",
          left: "50%",
          top: "50%",
          transform: "translate(-50%, -50%)"
        });
        // 将span添加到div中
        progressDiv.append(progressSpan);
        var simvalue = parseFloat(res_Str['simvalue']);
        updateProgress(simvalue);

     })
    })
 })


//显示进度条


