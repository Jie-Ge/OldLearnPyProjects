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

url1 = "./data/apply_tec_dvlp_map.csv"
// url2 = "./data/apply_tec_dvlp_map.csv"

data1 = getcsv(url1);
console.log(data1);
console.log("dataType: "+ typeof(data1));
console.log("data[0]: " + Object.values(data1[0]));
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
let year = [];
let applicant = [];
let applicant_obj = {};
let aply_after_rmv = [];
for(row = 0; row < data1.length; row++){
  let value_ = Object.values(data1[row]);
  year.push(value_[0]);
  for(i = 1; i < value_.length; i+=2){
    if (value_[i] == "0" || i === value_.length-1) continue;
    if(!applicant.includes(value_[i])){
      applicant.push(value_[i]);
      applicant_obj[value_[i]] = [];  //value为列表类型
    }
  }
}
console.log("applicant: " + applicant);
console.log("year: " + year);

for(row = 0; row < data1.length; row++){
  aply_after_rmv = applicant.slice(0);
  let value_ = Object.values(data1[row]);
  for (i = 1; i < value_.length; i+=2) {
    if (value_[i] == "0" || i === value_.length-1) continue;
    applicant_obj[value_[i]].push(value_[i+1]);
    aply_after_rmv.remove(value_[i]);
  }

  for (j = 0; j < aply_after_rmv.length; j++) {
    applicant_obj[aply_after_rmv[j]].push("0");
  } 
}

console.log("applicant: " + applicant);
console.log("applicant_obj: " + applicant_obj["发明授权"]);
console.log("data[000]: " + typeof(Object.keys(applicant_obj)));

// 基于准备好的dom，初始化echarts实例
let myChart = echarts.init(document.getElementById('chart_plot_01'));

// 指定图表的配置项和数据

let legend_data = applicant;
console.log("legend_data: " + legend_data);
// let i;
i = 0;
let option = {
    tooltip: {
        trigger: 'axis',
    },
    legend: {
        type: 'scroll',
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
            boundaryGap: false,
            data: year,
           
        }
    ],
    yAxis: [
        {
            type: 'value'
        }
    ],
    series: serie_func(applicant, applicant_obj)
};

/*serie生成器*/
function serie_func(applicantss, applicant_object){  
 
    let serie = []; 
    for(let i = 0; i < applicantss.length; i++){
 
        let item = {  
            name: applicantss[i],
            type: 'line', 
            stack: '数量',
            data: Object.values(applicant_object)[i]
                    
        }  
        serie.push(item);  
    } 
      return serie;
} 


// 使用刚指定的配置项和数据显示图表。
myChart.setOption(option);




var ord_number = 1;
var tbody=document.querySelector("tbody");

let pat_rank_data = [];
let count_aply;
console.log("counts: " + Object.values(applicant_obj)[0]);

// 申请人与对应各类专利数量组成键值对
for (let i = 0; i < applicant.length; i++) {

    aply_count = {};
    let counts = Object.values(applicant_obj)[i];

    for (let j = 0; j < counts.length; j++) {
      aply_count[year[j]] = parseInt(counts[j]);
      
    }
    let aply_count_ord = objsortbyval(aply_count);
    let aply_ord = Object.keys(aply_count_ord);
    let count_ord = Object.values(aply_count_ord);
    console.log("key: " + aply_ord);
    console.log("value: " + count_ord);


    add_table(aply_ord, count_ord, applicant[i]);
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