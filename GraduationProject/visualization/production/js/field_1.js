// var dataList=[
//     {name:"南海诸岛",value:0},
'北京',
'天津',
'上海',
'重庆',
'河北',
'河南',
'云南',
'辽宁',
'黑龙江',
'湖南',
'安徽',
'山东',
'新疆',
'江苏',
'浙江',
'江西',
'湖北',
'广西',
'甘肃',
'山西',
'内蒙古',
'陕西',
'吉林',
'福建',
'贵州',
'广东',
'青海',
'西藏',
'四川',
'宁夏',
'海南',
'台湾',
'香港',
'澳门'
// ]

function getcsv(url) {
    let findata = []
    let record = $.ajax({
        url: url,
        async: false
    }).responseText;
    record = (record || "").split(/\n/);
    let title = record[0].split(",");
    record.shift();
    for(let i = 0; i < record.length - 1; i++) {
        let t = record[i].split(",");
        for(let j = 0; j < title.length; j++) {
            if(!findata[i]) {
                findata[i] = {};
            }
            findata[i][title[j].replace(/(^\s*)|(\s*$)/g, "")] = t[j];
        }
    }
    return findata
}

url = "./data/province_aply_count.csv"


data = getcsv(url);
console.log(data);
console.log("dataType: "+ typeof(data));
console.log("data[0]: " + Object.values(data[0]));
// 用于移除数组中指定元素
Array.prototype.indexOf = function(val) { 
    for (let i = 0; i < this.length; i++) { 
        if (this[i] == val) return i; 
    } 
    return -1; 
};  
Array.prototype.remove = function(val) { 
    let index = this.indexOf(val); 
        if (index > -1) { 
            this.splice(index, 1); 
        } 
};  



let obj = {};
let row;
let i;
let j;
let province = [];
var count = [];

let total_prov = ['北京','天津','上海','重庆','河北','河南','云南','辽宁',
'黑龙江','湖南','安徽','山东','江苏','浙江','江西','湖北','甘肃','山西',
'陕西','吉林','福建','贵州','广东','青海','四川','海南','台湾','香港','澳门',
'广西','新疆','内蒙古','宁夏','西藏',
"南海诸岛"]

for(row = 0; row < data.length; row++){
  let value_ = Object.values(data[row]);
  province.push(value_[0]);
  count.push(value_[1]);

  total_prov.remove(value_[0]);
}
console.log("province: " + province);
console.log("count: " + count);


for(i = 0; i < total_prov.length; i++){
    province.push(total_prov[i]);
    count.push("0");
}


// 基于准备好的dom，初始化echarts实例
let myChart = echarts.init(document.getElementById('chart_plot_01'));

// 指定图表的配置项和数据

// let i;
i = 0;

option = {
    tooltip: {
            formatter:function(params,ticket, callback){
                return params.seriesName+'<br />'+params.name+'：'+params.value
            }//数据格式化
        },
    visualMap: {
        min: 0,
        max: count[0],
        left: 'left',
        top: 'bottom',
        text: ['高','低'],//取值范围的文字
        inRange: {
            color: ['#e0ffff', '#006edd']//取值范围的颜色
        },
        show:true,//图注
        calculable : true
    },
    geo: {
        map: 'china',
        roam: true,//开启缩放和平移
        zoom:1.23,//视角缩放比例
        label: {
            normal: {
                show: true,
                fontSize:'10',
                color: 'rgba(0,0,0,0.7)'
            }
        },
        itemStyle: {
            normal:{
                borderColor: 'rgba(0, 0, 0, 0.2)'
            },
            emphasis:{
                areaColor: '#F3B329',//鼠标选择区域颜色
                shadowOffsetX: 0,
                shadowOffsetY: 0,
                shadowBlur: 20,
                borderWidth: 0,
                shadowColor: 'rgba(0, 0, 0, 0.5)'
            }
        }
    },
    toolbox: {
        show: true,
        orient : 'vertical',
        left: 'right',
        top: 'center',
        feature : {
            mark : {show: true},
            dataView : {show: true, readOnly: false},
            restore : {show: true},
            saveAsImage : {show: true}
        }
    },
    series : [
        {
            name: '信息量',
            type: 'map',
            geoIndex: 0,
            data: serie_func(province, count)
        }
    ]
};


/*serie生成器*/
function serie_func(prov, cout){  
 
    let serie_data = []; 
    for(let i = 0; i < prov.length; i++){
 
        let item = {  
            name: prov[i],
            value: cout[i]
                    
        }  
        serie_data.push(item);  
    } 
      return serie_data;
} 


myChart.setOption(option);
myChart.on('click', function (params) {
    alert(params.name);
});

/*  setTimeout(function () {
    myChart.setOption({
        series : [
            {
                name: '信息量',
                type: 'map',
                geoIndex: 0,
                data:dataList
            }
        ]
    });
},1000)*/