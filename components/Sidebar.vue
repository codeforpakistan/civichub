<script setup lang="ts">

const links=[[
  { label: 'Home', to: '/', icon: 'i-ic:baseline-home' },
  { label: 'Explore', to: '/explore', icon: 'i-ic:outline-explore' },
  { label: 'Nearby', to: '/nearby', icon: 'i-ic:outline-location-on' },
],[
  { label: 'About CivicHub', to: '/about', icon: 'i-ic:outline-info' },
  { label: 'Terms of Use', to: '/policies/terms', icon: 'i-ic:baseline-list-alt' },
  { label: 'Privacy Policy', to: '/policies/privacy', icon: 'i-ic:baseline-balance' },
  { label: 'Content Policy ', to: '/policies/content', icon: 'i-ic:baseline-menu-book' },
  { label: 'Contact Us', to: '/contact', icon: 'i-ic:baseline-mail-outline' },
  // { label: 'Subscribe', to: '/subscribe', icon: 'i-ic:baseline-notifications-none', }
]]

</script>

<template>
  <UVerticalNavigation :links="links" />
</template>