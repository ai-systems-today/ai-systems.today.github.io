---
title: "Contact"
date: 2023-10-01
draft: false
---
<link rel="stylesheet" href="{{ "contact.css" | relURL }}">
<div class="contact-grid">
  <div class="contact-item">
    <h2>Address</h2>
    <p>Paju tn 1a, 50603 Tartu, Tartu Maakond, Estonia</p>
  </div>
  <div class="contact-item">
    <h2>Google Map</h2>
    {{< google_map "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2091.123456789!2d26.123456789!3d58.123456789!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x1234567890abcdef:0x1234567890abcdef!2sPaju%20tn%201a,%2050603%20Tartu,%20Tartu%20Maakond,%20Estonia!5e0!3m2!1sen!2s!4v1234567890" >}}
  </div>
  <div class="contact-item">
    <h2>Send Us a Message</h2>
    {{< contact_form >}}
  </div>
  <div class="contact-item">
    <h2>Schedule a Meeting</h2>
    <a href="https://calendly.com/your-calendly-link" class="button">Connect on Calendly</a>
  </div>
</div>