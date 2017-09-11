var word_list = [
    { text: data_parce[0]["word"], weight: 19 }
    ,{ text: data_parce[1]["word"], weight: 17 }
    ,{ text: data_parce[2]["word"], weight: 17 }
    ,{ text: data_parce[3]["word"], weight: 16 }
    ,{ text: data_parce[4]["word"], weight: 16 }
    ,{ text: data_parce[5]["word"], weight: 15 }
    ,{ text: data_parce[6]["word"], weight: 13 }
    ,{ text: data_parce[7]["word"], weight: 13 }
    ,{ text: data_parce[8]["word"], weight: 13 }
    ,{ text: data_parce[9]["word"], weight: 13 }
    ,{ text: data_parce[10]["word"], weight: 12 }
    ,{ text: data_parce[11]["word"], weight: 12 }
    ,{ text: data_parce[12]["word"], weight: 12 }
    ,{ text: data_parce[13]["word"], weight: 12 }
    ,{ text: data_parce[14]["word"], weight: 12 }
    ,{ text: data_parce[15]["word"], weight: 12 }
    ,{ text: data_parce[16]["word"], weight: 12 }
    ,{ text: data_parce[17]["word"], weight: 12 }
    ,{ text: data_parce[18]["word"], weight: 12 }
    ,{ text: data_parce[19]["word"], weight: 12 }

  ];


$(function(){
    
    $("#tagcloud").jQCloud( word_list, {
        width: 500, height: 400
    });
});