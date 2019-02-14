


// getJSON(url,作用的返回内容)  # 接口单项请求请求成功
$.getJSON('http://127.0.0.1:5000/astock',function (content) {
    D_T = content.data;

     var chart = Highcharts.chart('container', {
       title: {

           text: '可视化测试'
       },
       subtitle: {
           text: '进场时点和成本(4800,-21.3)'
       },
         xAxis: {
             // ... 省略代码
             plotLines:[{
                 color:'green',            //线的颜色，定义为红色
                 dashStyle:'longdashdot',//标示线的样式，默认是solid（实线），这里定义为长虚线
                 value:4800,                //定义在哪个值上显示标示线，这里是在x轴上刻度为3的值处垂直化一条线
                 width:2                 //标示线的宽度，2px
             }]
         },
       yAxis: {
           opposite:true,
           title: {
               text: '收益率'
           },
           plotLines:[{
               color:'red',           //线的颜色，定义为红色
               dashStyle:'Dash',     //默认值，这里定义为实线
               value:-21.3,               //定义在那个值上显示标示线，这里是在x轴上刻度为3的值处垂直化一条线
               width:1.6                //标示线的宽度，2px
           }]

       },
       legend: {
           layout: 'vertical',
           align: 'right',
           verticalAlign: 'middle'
       },
       plotOptions: {
           series: {
               label: {
                   connectorAllowed: false
               }
               // pointStart: 2010
           }
       },
       series: [{
           name: '可视化测试',
           data:D_T,
           //　数据量太大这种方法就失效了！
       }],
       responsive: {
           rules: [{
               condition: {
                   maxWidth: 500
               },
               chartOptions: {
                   legend: {
                       layout: 'horizontal',
                       align: 'center',
                       verticalAlign: 'bottom'
                   }
               }
           }]
       }
});})



