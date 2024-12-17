---
title: "Welcome to AI SYSTEMS TODAY"
description: "AI SYSTEMS TODAY Homepage"
---

<!-- YouTube Video Embed -->
<iframe 
  id="ytplayer" 
  type="text/html" 
  width="570" 
  height="315"
  src="https://www.youtube.com/embed/N2A6DqjzOhI?enablejsapi=1&rel=0&iv_load_policy=3"
  frameborder="0" 
  allowfullscreen>
</iframe>

<!-- YouTube IFrame Player API Script -->
<script async src="https://www.youtube.com/iframe_api"></script>

<script>
  // Load YouTube API and Initialize Player
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

<!-- Meeting Button -->
<br>
<a href="https://calendly.com/contact-ai-systems-today/30min" target="_blank" style="text-decoration:none;">
  <button style="padding:10px 20px; background-color:#1f78b4; color:white; border:none; border-radius:5px; cursor:pointer;">
    Schedule a Meeting
  </button>
</a>
