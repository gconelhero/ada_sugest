var titles = [];
var reject = ["Nova guia", "Google", "Extensões"]
//  localStorage.clear()
chrome.tabs.onActivated.addListener(tab =>  {
    chrome.tabs.get(tab.tabId, current_tab_info => {
        if (titles.indexOf(current_tab_info.title) === -1 && 
            reject.indexOf(current_tab_info.title) === -1) { 
                if (titles.length ===8 ) {
                    titles.shift()
                    titles.push(current_tab_info.title)
                    localStorage.setItem("titles", 
                        titles.join([separador=" , "]))
                        console.log(titles);
                } else {
                    titles.push(current_tab_info.title)
                    localStorage.setItem("titles", 
                        titles.join([separador=" , "]))
                    console.log(titles);
                }         
        };
    });
});    

function callApi() {
    const req = new XMLHttpRequest();
    const baseUrl = "http://192.168.0.16:5000/body_dict/insert";
    const data = localStorage.getItem("titles");
    req.onreadystatechange = function() {
        if (req.readyState == XMLHttpRequest.DONE) {
            localStorage.setItem("ada", "")
            localStorage.setItem("ada", req.responseText)
            alert(localStorage.getItem("ada"));
        }
    }
    req.open("POST", baseUrl, true); 
    req.setRequestHeader('Content-type', 'application/x-www-form-urlencoded; charset=UTF-8');
    req.send("titles=" + data)

};

document.addEventListener('DOMContentLoaded', function() {
    var run = document.getElementById('run');
    if (run) {
        run.addEventListener('click', function() {
            callApi();
        
        });
    };
});

document.addEventListener('DOMContentLoaded', function() {
    var open = document.getElementById('open');
    if (open) {
        open.addEventListener('click', function() {
            var new_url = localStorage.getItem("ada")
            chrome.tabs.create({url: new_url});
        
        });
    };
});
chrome.webRequest.onCompleted.addListener(
    function(details) {
      console.log(details);
    },
    {urls: ["http://192.168.0.16:5000/*"]}
  );