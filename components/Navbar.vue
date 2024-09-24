<script setup lang="ts">

const user = useSupabaseUser()

</script>

<template>
  <UContainer class="flex" :ui="{ constrained: 'min-w-full', base: '' }">
    <Drawer class="flex md:hidden" />
    <SiteTitle class="py-2" />
    <UFormGroup class="p-2 mx-auto grow-1">
      <UInput icon="i-ic:outline-search" color="white" :trailing="false" placeholder="Search..." />
    </UFormGroup>
    <div class="flex items-center">
      <UButton v-if="user" to="/activities/create" icon="i-ic:outline-plus" color="gray" variant="ghost" size="xl" :ui="{ rounded: 'rounded-full' }" />
      <UButton v-else to="/login" icon="i-ic:baseline-login" color="gray" variant="ghost" size="xl" :ui="{ rounded: 'rounded-full' }" />
      <UButton v-if="user" to="/account" icon="i-ic:outline-person" color="gray" variant="ghost" size="xl" :ui="{ rounded: 'rounded-full' }" />
      <ThemeToggle />
    </div>
  </UContainer>
</template>

