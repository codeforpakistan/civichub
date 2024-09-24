<script setup lang="ts">
useHead({
  title: 'Civic Hub',
  meta: [
    { name: 'description', content: 'My amazing site.' }
  ],
})
</script>

<template>
  <NuxtLayout>
    <NuxtLoadingIndicator />
    <NuxtPage />
  </NuxtLayout>
</template>
