#创建学籍参数化输入的数据
input_addschoolrolldata=[{"firstname":"李","lastname":"苏和","formername":"李苏","sexval":"1","engfamilyname":"li","engfirstname":"suhe",
                          "datatime":"readonly","birth":"19970923","countrycodeval":"46","nationval":"1","politicalval":"4","place":"tianjin",
                          "cardtypeval":"1","cardno":"121083199510201041","visaeffectivedate":"20300902","marriage":"1","language":"3","maindarin":"1",
                          "snum":"2017010002","department":"12011602","grade":"14","trainlevel":"7","yearattr":"value","year":"3","program":"85","stutype":"12","studytype":"8",
                          "butary":"5","ingrade":"14","enterdate":"20170901","enddate":"20200701","stucode":"2017020002","stusoursettype":"1","area":"1"},
                         {"firstname":"王","lastname":"苏","formername":"王明","sexval":"1","engfamilyname":"wang","engfirstname":"su",
                          "datatime":"readonly","birth":"19970921","countrycodeval":"46","nationval":"1","politicalval":"4","place":"tianjin",
                          "cardtypeval":"1","cardno":"121083199510201042","visaeffectivedate":"20300902","marriage":"1","language":"3","maindarin":"1",
                          "snum":"2017010003","department":"12011602","grade":"14","trainlevel":"7","yearattr":"value","year":"3","program":"85","stutype":"12","studytype":"8",
                          "butary":"5","ingrade":"14","enterdate":"20170901","enddate":"20200701","stucode":"2017020003","stusoursettype":"1","area":"1"}
                         ]

assert_data=[{"snum":["2017010002"]},{"snum":["2017010003"]}]

assert_data=[{"snum":"2017010002"},{"snum":"2017010003"}]