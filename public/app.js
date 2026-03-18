let tracks = [];
let current = 0;

async function load() {
  const res = await fetch('/api/tracks');
  tracks = await res.json();
  play(0);
}

function play(i) {
  current = i;
  const track = tracks[i];
  const audio = document.getElementById('audio');
  audio.src = track.file;
  audio.play();
}

function toggle() {
  const audio = document.getElementById('audio');
  audio.paused ? audio.play() : audio.pause();
}

function next() { play((current+1)%tracks.length); }
function prev() { play((current-1+tracks.length)%tracks.length); }

window.onload = load;
