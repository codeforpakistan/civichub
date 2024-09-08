<script setup lang="ts">
const isOpen = ref(false)
const route = useRoute()

const links=[[
  { label: 'Home', to: '/', icon: 'i-mdi:home', },
  { label: 'Explore', to: '/explore', icon: 'i-mdi:compass-outline', },
  { label: 'Nearby', to: '/nearby', icon: 'i-mdi:map-marker-outline', },
  { label: 'About', to: '/about', icon: 'i-mdi:information-outline', },
  { label: 'Login', to: '/login', icon: 'i-mdi:login', },
],[
  { label: 'Contact', to: '/contact' },
  { label: 'Subscribe', to: '/subscribe' }
]]

</script>

<template>
  <div>
    <UButton
      icon="i-ic:round-menu"
      size="xl"
      color="gray"
      variant="ghost"
      @click="isOpen = true"
    />

    <USlideover v-model="isOpen" side="left">
      
      <UCard class="flex flex-col flex-1" :ui="{ body: { base: 'flex-1' }, ring: '', divide: 'divide-y divide-gray-100 dark:divide-gray-800' }">
        <template #header>
          <div class="flex items-center justify-between">
            <SiteTitle />
            <UButton color="gray" variant="ghost" icon="i-heroicons-x-mark-20-solid" class="-my-1" @click="isOpen = false" />
          </div>
        </template>
        <UVerticalNavigation class="mb-2" :links="links" />
      </UCard>
    </USlideover>
  </div>
</template>

