const slides=document.querySelectorAll('.slide');
let currentSlide=0;
const totalSlides=slides.length;
const intervalTime=3000;
function nextSlide(){
    if(slides.length===0)return;
    slides[currentSlide].classList.remove('active');

    currentSlide=(currentSlide+1)%totalSlides;
    slides[currentSlide].classList.add('active');
}
function prevSlide(){
    if(slides.length===0)return;
    currentSlide=(currentSlide-1+totalSlides)%totalSlides;
    slides[currentSlide].classList.add('active');

}
function autoSlide()
{
    if(slides.lengtn===0)return;
    nextSlide();
}
const slideInterval=setInterval(autoSlide,intervalTime);
document.getElementById('prevBtn').addEventListener('click',()=>{
    clearInterval(slideInterval);
    prevSlide();
});
document.getElementById('nextBtn').addEventListener('click',()=>{
    clearInterval(slideInterval);
    nextSlide();
});