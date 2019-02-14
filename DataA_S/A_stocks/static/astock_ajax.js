// 尝试写一个异步请求,应该是获取接口的数组数据之后,
//还需要再重新遍历一次
//遍历一个数组(请求一次,遍历一次,过了一道,这才好同步)


//  网上有一个例子是把ajax请求数据并遍历,最后返回一个数组,放在highcharts的series的data的值中

$(function){
    var chart = Highcharts.chart('container', {
        title: {
            text: '可视'
        },
        subtitle: {
            text: '进程成本-21.3'
        },
        yAxis:{
			lineWidth: 1,
			opposite: true,
			title: {
				text: 'Secondary Axis'
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
            name: '进程成本-21.3',
            data:(function () {
                var ajax_data = [],

                $.ajax({
                    url:"http://127.0.0.1:5000/astock"
                    type:"GET",
                    async:false, // 很关键默认情况下是异步的,所以必须加上false
                    data:"json",
                    success:function(json){
                        for(i=0,i<json.valuelist.length;i++){
                            ajax_data.push({
                                x:i,
                                y:json.valuelist[i]
                            });
                        }
                    },
                    error:function (result) {
                        alert('出错了');
                    }
                }
                return ajax_data;
            })

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



