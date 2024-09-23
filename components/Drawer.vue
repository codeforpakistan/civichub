<script setup lang="ts">

const isOpen = ref(false)

const links=[[
  { label: 'Home', to: '/', icon: 'i-ic:baseline-home', },
  { label: 'Explore', to: '/explore', icon: 'i-ic:outline-explore', },
  { label: 'Nearby', to: '/nearby', icon: 'i-ic:outline-location-on', },
  { label: 'Login', to: '/login', icon: 'i-ic:outline-login', },
],[
  { label: 'About CivicHub', to: '/about', icon: 'i-ic:outline-info', },
  { label: 'Terms of Use', to: '/policies/terms', icon: 'i-ic:baseline-list-alt', },
  { label: 'Privacy Policy', to: '/policies/privacy', icon: 'i-ic:baseline-balance', },
  { label: 'Content Policy ', to: '/policies/content', icon: 'i-ic:baseline-menu-book', },
  { label: 'Contact Us', to: '/contact', icon: 'i-ic:baseline-mail-outline' },
  { label: 'Subscribe', to: '/subscribe', icon: 'i-ic:baseline-notifications-none' }
]]

const socials = [
  { icon: 'i-fe:facebook', to: 'https://www.facebook.com/CodeforPK' },
  { icon: 'i-fe:instagram', to: 'https://www.instagram.com/codeforpakistan/' },
  { icon: 'i-fe:twitter', to: 'https://twitter.com/CodeforPakistan' },
  { icon: 'i-fe:youtube', to: 'https://www.youtube.com/@codeforpk' },
]

</script>

<template>
  <div>
    <UButton icon="i-ic:round-menu" size="xl" color="gray" variant="ghost" @click="isOpen = true" />

    <USlideover v-model="isOpen" side="left">
      
      <UCard class="flex flex-col flex-1" :ui="{ body: { base: 'flex-1' }, ring: '', divide: 'divide-y divide-gray-100 dark:divide-gray-800' }">
        <template #header>
          <div class="flex items-center justify-between">
            <SiteTitle />
            <UButton color="gray" variant="ghost" icon="i-heroicons-x-mark-20-solid" class="-my-1" @click="isOpen = false" />
          </div>
        </template>
        <UVerticalNavigation class="mb-2" :links="links" />
        <template #footer>
          <UHorizontalNavigation :links="socials" />
          <div class="col-span-12 xl:col-span-6 py-4 text-sm opacity-50">
            <p>Site design / logo © 2013-2024 <ULink class="underline" to="https://codeforpakistan.org">Code for Pakistan</ULink>.</p>
            <p>Content licensed under a <ULink class="underline" to="https://creativecommons.org/licenses/by/4.0/">Creative Commons</ULink> license.</p>
          </div>
        </template>
      </UCard>
    </USlideover>
  </div>
</template>

