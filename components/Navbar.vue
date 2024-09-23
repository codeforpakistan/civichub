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
  <nav class="flex p-2 md:p-4">
    <Drawer />
    <SiteTitle class="p-1" />
    <span class="grow"></span>
    <UHorizontalNavigation :links="links" class="hidden md:flex" :ui="{ container: 'flex justify-center items-center w-full gap-2' }" />
    <div class="flex justify-end items-center">
      <UButton v-if="user" to="/activities/create" icon="i-ic:outline-plus" color="gray" variant="ghost" size="xl" :ui="{ rounded: 'rounded-full' }" />
      <UButton v-else to="/login" icon="i-ic:baseline-login" color="gray" variant="ghost" size="xl" :ui="{ rounded: 'rounded-full' }" />
      <UButton icon="i-ic:outline-search" color="gray" variant="ghost" size="xl" :ui="{ rounded: 'rounded-full' }" />
      <UButton v-if="user" to="/account" icon="i-ic:outline-person" color="gray" variant="ghost" size="xl" :ui="{ rounded: 'rounded-full' }" />
      <UButton @click="refreshAll" icon="i-ic:outline-refresh" color="gray" variant="ghost" size="xl" :ui="{ rounded: 'rounded-full' }" />
      <ThemeToggle />
    </div>
  </nav>
</template>

