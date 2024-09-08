<script setup lang="ts">

const user = useSupabaseUser()

const links = [
  { label: 'Home', to: '/' },
  { label: 'Explore', to: '/explore' },
  { label: 'Nearby', to: '/nearby' },
  { label: 'About', to: '/about' },
]

const refreshAll = async () => {
  await refreshNuxtData()
}
</script>

<template>
  <nav class="flex py-2 md:py-4">
    <Drawer class="block md:hidden" />
    <SiteTitle class="p-1" />
    <span class="grow"></span>
    <UHorizontalNavigation :links="links" class="hidden md:flex" :ui="{ container: 'flex justify-center items-center w-full gap-4' }" />
    <div class="flex justify-end items-center">
      
      <UButton to="/activities/create" icon="i-mdi:plus" color="gray" variant="ghost" size="xl" :ui="{ rounded: 'rounded-full' }" />
      <UButton icon="i-mdi:magnify" color="gray" variant="ghost" size="xl" :ui="{ rounded: 'rounded-full' }" />
      <UButton v-if="user" to="/account" icon="i-mdi:account-outline" variant="ghost" color="gray" size="xl" :ui="{ rounded: 'rounded-full' }" />
      <UButton @click="refreshAll" icon="i-mdi:refresh" variant="ghost" color="gray" size="xl" :ui="{ rounded: 'rounded-full' }" />
      <ThemeToggle />
    </div>
  </nav>
</template>

