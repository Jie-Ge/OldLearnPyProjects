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

url = "./data/applicant_rank.csv"


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
let applicant = [];
let patent_cla = [];
let count_of_aply = []; //
let patent_obj = {};
let pat_after_rmv = [];
for(row = 0; row < data.length; row++){
  let value_ = Object.values(data[row]);
  applicant.push(value_[0]);
  for(i = 1; i < value_.length; i+=2){
    if (value_[i] == "0" || i === value_.length-1) continue;
    if(!patent_cla.includes(value_[i])){
      patent_cla.push(value_[i]);
      patent_obj[value_[i]] = [];
    }
  }
}
console.log("patent_cla: " + patent_cla);
console.log("applicant: " + applicant);

for(row = 0; row < data.length; row++){
  pat_after_rmv = patent_cla.slice(0);
  let value_ = Object.values(data[row]);
  let counts = 0; //
  for (i = 1; i < value_.length; i+=2) {
    if (value_[i] == "0" || i === value_.length-1) continue;
    patent_obj[value_[i]].push(value_[i+1]);
    pat_after_rmv.remove(value_[i]);
    counts += parseInt(value_[i+1]); //
  }

  count_of_aply.push(counts); // ...


  for (j = 0; j < pat_after_rmv.length; j++) {
    patent_obj[pat_after_rmv[j]].push("0");
  } 
}

console.log("patent_cla: " + patent_cla);
console.log("patent_obj: " + patent_obj["发明授权"]);
console.log("data[000]: " + count_of_aply);


function barFun(){

  // 基于准备好的dom，初始化echarts实例
  let myChart = echarts.init(document.getElementById('chart_plot_01'));

  // 指定图表的配置项和数据

  let legend_data = patent_cla;
  console.log("legend_data: " + legend_data);

  let option = {
      tooltip: {
          trigger: 'axis',
          axisPointer: {            // 坐标轴指示器，坐标轴触发有效
              type: 'shadow'        // 默认为直线，可选为：'line' | 'shadow'
          }
      },
      legend: {
          data: legend_data
      },
      toolbox: {
          show: true,
          orient: 'vertical',
          left: 'right',
          top: 'center',
          feature: {
              mark: {show: true},
              dataView: {show: true, readOnly: false},
              magicType: {show: true, type: ['line', 'bar', 'stack', 'tiled']},
              restore: {show: true},
              saveAsImage: {show: true}
          }
      },
      grid: {
          left: '3%',
          right: '4%',
          bottom: '3%',
          containLabel: true
      },
      xAxis: [
          {
              type: 'category',
              data: applicant,
              axisLabel : {//坐标轴刻度标签的相关设置。
                  interval:0, //间隔
                  rotate:"45"
              }
          }
      ],
      yAxis: [
          {
              type: 'value'
          }
      ],
      series: serie_barFunc(patent_cla, patent_obj)
  };

  myChart.clear();
  // 使用刚指定的配置项和数据显示图表。
  myChart.setOption(option);

}

barFun();

/*serie生成器*/
function serie_barFunc(patent_class, patent_object){  
 
    let serie = []; 
    for(let i = 0; i < patent_class.length; i++){
 
        let item = {  
            name: patent_class[i],
            type: 'bar', 
            stack: '数量',
            data: Object.values(patent_object)[i]
                    
        }  
        serie.push(item);  
    } 
      return serie;
} 


function pieFun(){

  // 基于准备好的dom，初始化echarts实例
  let myChart = echarts.init(document.getElementById('chart_plot_01'));
  
  // 指定图表的配置项和数据

  let legend_data = applicant.concat(patent_cla);
  console.log("legend_data11111: " + legend_data);

  let option1 = {
    tooltip: {
        trigger: 'item',
        formatter: '{a} <br/>{b}: {c} ({d}%)'
    },
    legend: {
        orient: 'vertical',
        left: 10,
        data: ['直达', '营销广告', '搜索引擎', '邮件营销', '联盟广告', '视频广告', '百度', '谷歌', '必应', '其他']
    },
    series: [
        {
            name: '专利类型',
            type: 'pie',
            selectedMode: 'single',
            radius: [0, '30%'],

            label: {
                position: 'inner'
            },
            labelLine: {
                show: false
            },
            data: serie_patFunc()
        },
        {
            name: '申请人: 申请量',
            type: 'pie',
            radius: ['40%', '55%'],
            label: {
                formatter: '{a|{a}}{abg|}\n{hr|}\n  {b|{b}：}{c}  {per|{d}%}  ',
                backgroundColor: '#eee',
                borderColor: '#aaa',
                borderWidth: 1,
                borderRadius: 4,
                shadowBlur:3,
                shadowOffsetX: 2,
                shadowOffsetY: 2,
                shadowColor: '#999',
                padding: [0, 7],
                rich: {
                    a: {
                        color: '#999',
                        lineHeight: 22,
                        align: 'center'
                    },
                    // abg: {
                    //     backgroundColor: '#333',
                    //     width: '100%',
                    //     align: 'right',
                    //     height: 22,
                    //     borderRadius: [4, 4, 0, 0]
                    // },
                    hr: {
                        borderColor: '#aaa',
                        width: '100%',
                        borderWidth: 0.5,
                        height: 0
                    },
                    b: {
                        fontSize: 16,
                        lineHeight: 33
                    },
                    per: {
                        color: '#eee',
                        backgroundColor: '#334455',
                        padding: [2, 4],
                        borderRadius: 2
                    }
                }
            },
            data: serie_aplyFunc()
        }
    ]
};
  
  myChart.clear();
  // 使用刚指定的配置项和数据显示图表。
  myChart.setOption(option1);
}


function serie_patFunc(){
  let serie = []; 
  let values1 = [412, 92, 1];
  let pat1 = ['发明', '发明授权', '课题'];
    for(let i = 0; i < patent_cla.length; i++){
 
        let item = {  
            value: values1[i],
            name: pat1[i],
        }  
        serie.push(item);  
    } 
      return serie;
}


function serie_aplyFunc(){
  let serie = []; 
    for(let i = 0; i < applicant.length; i++){
 
        let item = {  
            value: count_of_aply[i],
            name: applicant[i],
        }  
        serie.push(item);  
    } 
      return serie;

}



// ****** 表格 *********

var ord_number = 1;
var tbody=document.querySelector("tbody");

let pat_rank_data = [];
let count_aply;
console.log("counts: " + Object.values(patent_obj)[0]);

// 申请人与对应各类专利数量组成键值对
for (let i = 0; i < patent_cla.length; i++) {

    aply_count = {};
    let counts = Object.values(patent_obj)[i];

    for (let j = 0; j < counts.length; j++) {
      aply_count[applicant[j]] = parseInt(counts[j]);
      
    }
    let aply_count_ord = objsortbyval(aply_count);
    let aply_ord = Object.keys(aply_count_ord);
    let count_ord = Object.values(aply_count_ord);
    console.log("key: " + aply_ord);
    console.log("value: " + count_ord);


    add_table(aply_ord, count_ord, patent_cla[i]);
    mergeCell('table_test', 0, 0, 1);

}

// 对象按value（int型）进行排序
function objsortbyval(obj1) {
  let keyArr = [],valArr = [];
  for (let key in obj1) {
    keyArr.push(key);
    valArr.push(obj1[key]);
  }
  for (let i = 0, len = valArr.length; i < len; i++) {
    for (let j = 0; j < len - i; j++) {
      let keyTemp, valTemp;
      if (valArr[j] < valArr[j + 1]) {
        valTemp = valArr[j];
        valArr[j] = valArr[j + 1];
        valArr[j+1] = valTemp;
        keyTemp = keyArr[j];
        keyArr[j] = keyArr[j + 1];
        keyArr[j+1] = keyTemp;
      }
    }
  }
  let newobj={};
  for(let i=0;i<valArr.length;i++){
    newobj[keyArr[i]]=valArr[i];
  }
  return newobj;
}
 
// 动态添加表格
function add_table(aply_ord, count_ord, pat_cla){
  let datas = [];
  for (let i = 0; i < aply_ord.length; i++) {
    let item = {
      'order': ord_number,
      'pat_class': pat_cla,
      'aply': aply_ord[i],
      'count': count_ord[i],
    };
    datas.push(item);
    ord_number++;
  }
  
  for(let i = 0;i < datas.length; i++){
    let tr = document.createElement("tr");
    
    tbody.appendChild(tr);
    for(let k in datas[i]){   //里面的for循环是列
      let td = document.createElement("td");  //创建单元格
      if(i==0 && k == 'pat_class'){
        // tr.setAttribute("style","rowspan="10"");//一次添加多个
        td.style.rowspan="10";//style.样式名=样式值;
      }
      tr.appendChild(td);
      
      td.innerHTML = datas[i][k]; //把对象里面的属性值 datas[i][k]给td
    }
  }
}


//合并相同单元格（如果endRow传0代表合并所有行）
function mergeCell(table1, startRow, endRow, col) {
  let tb = document.getElementById(table1);
  if(!tb || !tb.rows || tb.rows.length <= 0) {
      return;
  }
  if(col >= tb.rows[0].cells.length || (startRow >= endRow && endRow != 0)) {
      return;
  }
  if(endRow == 0) {
      endRow = tb.rows.length - 1;
  }
  for(let i = startRow; i < endRow; i++) {
      if(tb.rows[startRow].cells[col].innerHTML == tb.rows[i + 1].cells[col].innerHTML) { //如果相等就合并单元格,合并之后跳过下一行
          tb.rows[i + 1].removeChild(tb.rows[i + 1].cells[col]);
          tb.rows[startRow].cells[col].rowSpan = (tb.rows[startRow].cells[col].rowSpan) + 1;
      } else {
          mergeCell(table1, i + 1, endRow, col);
          break;
      }
  }
}