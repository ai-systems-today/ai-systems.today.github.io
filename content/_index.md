---
title: "Welcome to AI SYSTEMS TODAY"
description: "AI SYSTEMS TODAY Homepage"
---

<style>
/* Title and Subtitle Adjustments */
.page-content h1 {
  margin-bottom: 0.5rem; /* Decrease space below the title */
  font-size: 2.5rem; /* Slightly larger title for emphasis */
  line-height: 1.2; /* Adjust line height for compact spacing */
  text-align: center; /* Center align the title */
}

.page-content p {
  margin-top: 0.2rem; /* Minimal space above the subtitle */
  margin-bottom: 1rem; /* Balanced space below subtitle */
  font-size: 1.2rem; /* Adjust font size */
  text-align: center; /* Center align subtitle */
}

/* Video Container */
.responsive-video {
  position: relative;
  width: 100%;
  max-width: 720px; /* Restrict width for better layout */
  margin: 1rem auto 0.5rem; /* Reduce space above and below video */
  padding-bottom: 56.25%; /* Maintain 16:9 aspect ratio */
  height: 0;
  overflow: hidden;
}

.responsive-video iframe {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}

/* Button Spacing */
.meeting-button {
  display: block;
  margin: 1rem auto; /* Center button and reduce top spacing */
  padding: 10px 20px;
  background-color: #1f78b4;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-size: 1rem;
  text-align: center;
}

.meeting-button:hover {
  background-color: #155a8a;
}
</style>

  <!-- Subtitle -->
  {{< lead >}}
  Empowering your business with cutting-edge AI solutions
  {{< /lead >}}
  <!-- <p>Empowering your business with cutting-edge AI solutions</p> -->

  <!-- Video -->
  <div class="responsive-video">
    <iframe
      id="ytplayer"
      src="https://www.youtube.com/embed/N2A6DqjzOhI?enablejsapi=1&rel=0&iv_load_policy=3"
      frameborder="0"
      allowfullscreen>
    </iframe>
  </div>

  <!-- Meeting Button -->
  <a href="https://calendly.com/contact-ai-systems-today/30min" target="_blank">
    <button class="meeting-button">Schedule a Meeting</button>
  </a>
</div>
