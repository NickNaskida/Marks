/*
//Movement animation
const card = document.querySelector('.card');
const right = document.querySelector('.right');
//items
const avatar = document.querySelector('.avatar img');
const description = document.querySelector('.info h3');
const title = document.querySelector('.title');
const social1 = document.querySelector('.butt1');
const social2 = document.querySelector('.butt2');
const social3 = document.querySelector('.butt3');
const contacts = document.querySelector('.contacts');


//Moving animation event
//right.addEventListener('mousemove', (e) => {
 //let xAxis = ((window.innerWidth) /1.6 - e.pageX) /20
 //let yAxis = (window.innerHeight /1.6 - e.pageY) /20;

 //card.style.transform = `rotateY(${xAxis}deg) rotateX(${yAxis}deg)`
//});
//animate in
right.addEventListener('mouseenter', e =>{
	card.style.transition = 'none';
	//popout
	social1.style.transform = "translateZ(60px)";
	social2.style.transform = "translateZ(60px)";
	social3.style.transform = "translateZ(60px)";
	title.style.transform = "translateZ(60px)";
	description.style.transform = "translateZ(60px)";
	avatar.style.transform = "translateZ(60px)";
	contacts.style.transform = "translateZ(60px)";
})

//animate out
right.addEventListener('mouseleave', e => {
	card.style.transform = `rotateY(0deg) rotateX(0deg)`;
	card.style.transition = 'all 0.5s ease'; 
	//popin
	social1.style.transform = "translateZ(0px)";
	social2.style.transform = "translateZ(0px)";
	social3.style.transform = "translateZ(0px)";
	title.style.transform = "translateZ(0px)";
	description.style.transform = "translateZ(0px)";
	avatar.style.transform = "translateZ(0px)";
	contacts.style.transform = "translateZ(0px)";


});*/


$(function() {
	/* burger menu navToggle */
	let nav = $("#nav")
	$("#navToggle").on("click", function(event) {
		event.preventDefault();

		nav.toggleClass("show");
	})

});