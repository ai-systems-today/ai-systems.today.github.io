---
title: "Welcome to AI SYSTEMS TODAY"
description: "AI SYSTEMS TODAY Homepage"
---

<style>
/* Ensure the video container is responsive */
.video-container {
  position: relative;
  width: 100%;
  max-width: 960px; /* Add a max width for larger screens */
  margin: 0 auto; /* Center horizontally */
  padding-bottom: 56.25%; /* 16:9 aspect ratio */
  height: 0;
  overflow: hidden;
  display: block; /* Ensure it's a block element */
}

.video-container iframe {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  border: none;
}

/* Parent container for alignment and spacing */
.page-content {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  margin-top: 2rem;
}

.meeting-button {
  margin-top: 1rem;
  padding: 10px 20px;
  background-color: #1f78b4;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-size: 1rem;
  text-decoration: none;
  display: inline-block;
}

.meeting-button:hover {
  background-color: #155a8a;
}
</style>

<!-- Content Wrapper -->
<div class="page-content">
  <!-- <h1>AI SYSTEMS TODAY</h1> -->
  <p>Empowering your business with cutting-edge AI solutions</p>

  <!-- Responsive YouTube Video -->
  <div class="video-container">
    <iframe
      id="ytplayer"
      src="https://www.youtube.com/embed/N2A6DqjzOhI?enablejsapi=1&rel=0&iv_load_policy=3"
      allowfullscreen>
    </iframe>
  </div>

  <!-- Meeting Button -->
  <a href="https://calendly.com/contact-ai-systems-today/30min" target="_blank" class="meeting-button">
    Schedule a Meeting
  </a>
</div>

<!-- YouTube IFrame Player API Script -->
<script async src="https://www.youtube.com/iframe_api"></script>
<script>
  var player;
  function onYouTubeIframeAPIReady() {
    player = new YT.Player('ytplayer', {
      events: {
        'onStateChange': onPlayerStateChange
      }
    });
  }

  function onPlayerStateChange(event) {
    if (event.data === YT.PlayerState.ENDED) {
      player.seekTo(0);
      player.pauseVideo();
    }
  }
</script>
