<script setup lang="ts">

const links = [[
  { label: 'About', to: '/about' },
  { label: 'Terms', to: '/policies/terms' },
  { label: 'Privacy', to: '/policies/privacy' },
  { label: 'Content', to: '/policies/content' },
],[
  { icon: 'i-fe:facebook', to: 'https://www.facebook.com/CodeforPK' },
  { icon: 'i-fe:instagram', to: 'https://www.instagram.com/codeforpakistan/' },
  { icon: 'i-fe:twitter', to: 'https://twitter.com/CodeforPakistan' },
  { icon: 'i-fe:youtube', to: 'https://www.youtube.com/@codeforpk' },
]]

const socials = [
]

</script>

<template>
  <footer>
    <UDivider />
    <nav class="grid grid-cols-12">
      <div class="col-span-12 xl:col-span-6 py-4 text-sm opacity-50">Site design / logo © 2013-2024 <ULink class="underline" to="https://codeforpakistan.org">Code for Pakistan</ULink>. Content licensed under a <ULink class="underline" to="https://creativecommons.org/licenses/by/4.0/">Creative Commons</ULink> license.</div>
      <div class="col-span-12 xl:col-span-6">
        <UHorizontalNavigation :links="links" :ui="{ container: 'flex justify-around xl:justify-end items-center w-full' }" />
      </div>
    </nav>
  </footer>
</template>