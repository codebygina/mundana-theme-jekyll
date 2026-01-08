---
title: "Kontakt"
permalink: "/contact.html"
---

<form action="https://formspree.io/f/mgedaald" method="POST">    
<p class="mb-4">Du möchtest einen Beitrag auf {{site.name}} veröffentlichen? Oder einfach einen Kommentar an uns senden? Wir freuen uns auf deine Nachricht!</p>
<div class="form-group row">
<div class="col-md-6">
<input class="form-control" type="text" name="name" placeholder="Name*" required>
</div>
<div class="col-md-6">
<input class="form-control" type="email" name="_replyto" placeholder="E-mail Adresse*" required>
</div>
</div>
<textarea rows="8" class="form-control mb-3" name="message" placeholder="Nachricht*" required></textarea>    
<input class="btn btn-success" type="submit" value="Absenden">
</form>

<br>
<div class='impressum'><strong>Impressum: </strong> Angaben gemäß § 5 TMG,
Klaus Brecht, 
Hermannstraße 21, 
12049 Berlin, 
<a href="{{site.baseurl}}/privacy-policy.html">Haftungsausschluss und Datenschutz</a> </div>
