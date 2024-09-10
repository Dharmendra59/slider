let tl = gsap.timeline();
tl.from('.rf', {
    y: 30,
    opacity: 0,
    duration: 3,
    scale: 0.2,

}, 'a')
tl.to('.rf', {
    y: -80,
    opacity: 0,
    duration: 5,
    delay: 2,

}, 'a')
tl.to('.main', {
    scale: -1,
    duration: 0
}, 'b')