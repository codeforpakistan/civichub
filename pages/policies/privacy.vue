<template>
  <main class="grid grid-cols-12">
    <div class="col-span-12 lg:col-span-3">
      <h1 class="text-5xl lg:text-7xl mb-8">Privacy Policy</h1>
    </div>
    <div class="col-span-12 lg:col-span-9">

      <h4 class="text-2xl mb-4 border-b border-gray-200 dark:border-gray-800">Introduction</h4>

      <dl class="grid grid-cols-12 mb-8">
        <dt class="col-span-2 font-bold">Purpose</dt>
        <dd class="col-span-10 opacity-75">This is the website for {% app_name %}. We protect your personal information using industry-standard
          safeguards.</dd>
        <dt class="col-span-2 font-bold">Sharing / Changes</dt>
        <dd class="col-span-10 opacity-75">We may share your information with your consent or as required by law, and we will always let you know when we
          make significant changes to this Privacy Policy.</dd>
      </dl>

      <h4 class="text-2xl mb-4 border-b border-gray-200 dark:border-gray-800">Information we collect</h4>

      <dl class="grid grid-cols-12 mb-8">
        <dt class="col-span-2 font-bold">Registration</dt>
        <dd class="col-span-10 opacity-75">When you create an account with us, we collect information (including your name and email address).</dd>
        <dt class="col-span-2 font-bold">Profile Information</dt>
        <dd class="col-span-10 opacity-75">We collect information when you fill out our registration forms. A complete form including personal and
          professional details – like your gender, age, occupation, education, among others – ends up as statistics in our
          services.</dd>
        <dt class="col-span-2 font-bold">Cookies</dt>
        <dd class="col-span-10 opacity-75">We use cookies and similar technologies to collect information.</dd>
        <dt class="col-span-2 font-bold">Log Files</dt>
        <dd class="col-span-10 opacity-75">We collect information from the devices and networks that you use to access our Service.</dd>
      </dl>
      <h4 class="text-2xl mb-4 border-b border-gray-200 dark:border-gray-800">How personal information is used</h4>

      <dl class="grid grid-cols-12 mb-8">
        <dt class="col-span-2 font-bold">Consent</dt>
        <dd class="col-span-10 opacity-75">You agree that information you provide on your profile can be seen used by us as described in this Privacy
          Policy and our <a href="{% url 'web:page' 'terms' %}">Terms of Use</a>.</dd>
        <dt class="col-span-2 font-bold">Communication</dt>
        <dd class="col-span-10 opacity-75">We communicate with you using email. We may send you messages relating to the availability of the
          Service, security, or other service-related issues.</dd>
        <dt class="col-span-2 font-bold">Service Development</dt>
        <dd class="col-span-10 opacity-75">We use the information you provide to us to conduct analysis, research and development, and to customize your
          experience and try to make it relevant and useful to you.</dd>
        <dt class="col-span-2 font-bold">Sharing Information</dt>
        <dd class="col-span-10 opacity-75">We do not share any personally identifying information that you provide to us. Non-identifying information is
          publically shared as part of our Service.</dd>
        <dt class="col-span-2 font-bold">Third Parties</dt>
        <dd class="col-span-10 opacity-75">We work with developers to build applications using our developer tools. If you have given an application access
          to your account, you can revoke that permission anytime. Also, you can opt out of providing information to
          developers through your connections.</dd>
        <dt class="col-span-2 font-bold">Polls and Surveys</dt>
        <dd class="col-span-10 opacity-75">We conduct our own surveys and polls and also help third parties do this type of research. Your participation in
          surveys or polls is up to you. You may also opt out of getting invitations to participate in surveys.</dd>
        <dt class="col-span-2 font-bold">Compliance</dt>
        <dd class="col-span-10 opacity-75">We may disclose your personal information if compelled by law, subpoena, or other legal process, or if necessary
          to enforce our User Agreement.</dd>
        <dt class="col-span-2 font-bold">International Use</dt>
        <dd class="col-span-10 opacity-75">We may process your information outside the country where you live.</dd>
      </dl>
      <h4 class="text-2xl mb-4 border-b border-gray-200 dark:border-gray-800">Choices &amp; Obligations</h4>

      <dl class="grid grid-cols-12 mb-8">
        <dt class="col-span-2 font-bold">Access / Closure</dt>
        <dd class="col-span-10 opacity-75">You can change your account information at any time by editing your profile, or by closing your account. You can
          also ask us for additional information we may have about your account.</dd>
        <dt class="col-span-2 font-bold">Data Retention</dt>
        <dd class="col-span-10 opacity-75">We keep your information for as long as your account is active or as needed. We may keep certain information
          even after you close your account if it is necessary to comply with our legal obligations, meet regulatory
          requirements, resolve disputes, prevent fraud and abuse, or enforce this agreement.</dd>
      </dl>
      <h4 class="text-2xl mb-4 border-b border-gray-200 dark:border-gray-800">Important Information</h4>

      <dl class="grid grid-cols-12 mb-8">
        <dt class="col-span-2 font-bold">Minimum Age</dt>
        <dd class="col-span-10 opacity-75">You have to meet our minimum age requirements to create an account.</dd>
        <dt class="col-span-2 font-bold">Marketing</dt>
        <dd class="col-span-10 opacity-75">We don't share any of your personal information with third parties for direct marketing.</dd>
        <dt class="col-span-2 font-bold">Security</dt>
        <dd class="col-span-10 opacity-75">We take privacy and security seriously and have enabled HTTPS access to our site, in addition to existing SSL
          access over mobile devices. Also, please know that the Internet is not a secure environment, so be careful and
          select strong passwords.</dd>
      </dl>
    </div>
  </main>
</template>