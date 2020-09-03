alert("Hello guys! Help me to make the cake!🙏\n\nConditions of contest: we cannot use any tag other than 4 div tags!");
alert("You can open and close the door of the oven by just clicking at it, to check if the cake is ready or not! The temperature meter is automatic!😍\nWait for the cake to get completely baked and served!");
// Cake is ready or not
var ready = false;
var used = false;

var count1 = 0;

var top1 = 13;
var height1 = 150;
var topchange1 = 0;

var rot = 0;

window.onload = function() {
    var d1 = document.getElementById("d1");
    var d2 = document.getElementById("d2");
    var d3 = document.getElementById("d3");
    var d4 = document.getElementById("d4");
    
    var body = document.getElementById("body");
    
    d3.onclick = function () {
        count1++;
        if (count1%2) {
            topchange1 = 1;
        }
        else {
            topchange1 = -1;
        }
    };
};

function changingd3() {
    if (top1 < 150 && top1 >= 13) {
        top1+=topchange1;
        height1-=topchange1;
    }
    
    else {
        if (top1 < 13) {
            top1++;
            height1--;
            topchange1 = 0;
        }
        else {
            top1--;
            height1++;
            topchange1 = 0;
        }
    }
    d3.style.top = `calc(30% + ${top1}px)`;
    d3.style.height = height1 + "px";
}

var t1 = setInterval(changingd3, 10);

function changingd4() {
    if (rot > 0 && top1 > 20) {
        rot-=3;
    }
    if (top1 <= 20 && rot < 135) {
        rot++;
    }
    d4.style.transform = `rotate(${rot}deg)`;
}
var t2 = setInterval(changingd4, 20);

//d2
var change = 0;
var r = 238; 
var g = 170;
var b = 187;
function changingd2() {
    if (change < 10){
        change += rot/8000;
    }
    else {
        clearInterval(t3);
        var t4 = setInterval(End, 10);
        alert("Your cake is ready! Now just open the door of the oven!");
        ready = true;
    }
    d2.style.top = `calc(30% + ${55+change}px)`;
    d2.style.height = `${40-change}px`;
    d2.style.background = `rgb(${r}, ${g}, ${b})`;
    r-=rot/700;
    g-=rot/700;
    b-=rot/660;
}

var t3 = setInterval(changingd2, 100);

function End() {
    if (rot > 0) {
        rot-=2;
    }
}

var i = 0;
var ichange = 1;
function Heatingcolor() {
    var r = 51+i*2;
    var gb = 15;
    
    d1.style.background = `linear-gradient(0deg, rgb(${r},${gb},${gb}) 42%, #000 42%, #000 46%, rgb(${r},${gb},${gb}) 46%) 13% 45% / 71% 90% , linear-gradient(0deg, #fffafa, #eeeeda) right / 20% 100% , linear-gradient(0deg, rgb(169,169,169), rgb(169,169,169)) 50% 50% / 100% 100%`;
    
    d1.style.backgroundRepeat = "no-repeat";
    
    i+=ichange;
    
    if (i > 60 && top1 < 20){
        ichange = -1;
    }
    if (i <= 10 && top1 < 20) {
        ichange = 1;
    }
    if (count1%2 && i > -2) {
        ichange = -4;
    }
    else if (count1%2) {
        ichange = 0;
    }
    
    if (i < -2) {
        i = -2;
    }
}

var t4 = setInterval(Heatingcolor, 35);
var caketop = 65;
var cakeleft = 80;
var myalert = true;
function CakeIsReady() {
    if (ready && top1 >= 150 && !used) {
        clearInterval(t1);
        used = true;
        d2.style.zIndex = "10";
    }
    
    else if (ready && top1 >= 150) {
        if (caketop < 235) {
            caketop+=0.85;
            cakeleft+=0.5;
        }
        
        if (caketop >= 235 && myalert) {
            alert("Woww! You have made the cake! Thanks for helping me in making the cake! And please upvote my code if you liked it!\n\n\n                                                    Jai AIMU");
            myalert = false;
        }
        d2.style.left = `calc(3% + ${cakeleft}px)`;
        
        d2.style.top = `calc(30% + ${caketop}px)`;
    }
}
var t5 = setInterval(CakeIsReady, 10);
