---
title: "Welcome to AI SYSTEMS TODAY"
description: "AI SYSTEMS TODAY Homepage"
---


<iframe id="ytplayer" type="text/html" width="570" height="315"
src="https://www.youtube.com/embed/N2A6DqjzOhI?enablejsapi=1&rel=0&iv_load_policy=3"
frameborder="0" allowfullscreen></iframe>

<!-- <iframe id="ytplayer" type="text/html" width="570" height="315"
src="https://www.youtube.com/embed/N2A6DqjzOhI?enablejsapi=1&rel=0&iv_load_policy=3"
frameborder="0" allowfullscreen></iframe> -->

<!-- <iframe id="ytplayer" type="text/html" width="570" height="315"
src="https://www.youtube.com/embed/N2A6DqjzOhI?enablejsapi=1"
frameborder="0" allowfullscreen></iframe> -->

<script>
  // Load the IFrame Player API code asynchronously.
  var tag = document.createElement('script');
  tag.src = "https://www.youtube.com/iframe_api";
  var firstScriptTag = document.getElementsByTagName['script'](0);
  var firstScriptTag = document.getElementsByTagName['script'](0);
  firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);

  // Create a YouTube player
  var player;
  function onYouTubeIframeAPIReady() {
    player = new YT.Player('ytplayer', {
      events: {
        'onStateChange': onPlayerStateChange
      }
    });
  }

  // When video state changes
  function onPlayerStateChange(event) {
    if (event.data == YT.PlayerState.ENDED) {
      // When video ends, seek to the start
      player.seekTo(0);
      player.pauseVideo(); // Make sure the video is paused at the start.
    }
  }
</script>

<br>

<a href="https://calendly.com/contact-ai-systems-today/30min" target="_blank" style="text-decoration:none;"><button style="padding:10px 20px; background-color:#1f78b4; color:white; border:none; border-radius:5px; cursor:pointer;">Schedule a Meeting</button></a>
