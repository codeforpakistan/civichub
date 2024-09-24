<script setup lang="ts">

const isOpen = ref(false)

const socials = [
  { icon: 'i-fe:facebook', to: 'https://www.facebook.com/CodeforPK' },
  { icon: 'i-fe:instagram', to: 'https://www.instagram.com/codeforpakistan/' },
  { icon: 'i-fe:twitter', to: 'https://twitter.com/CodeforPakistan' },
  { icon: 'i-fe:youtube', to: 'https://www.youtube.com/@codeforpk' },
]

</script>

<template>
  <div>
    <UButton icon="i-ic:round-menu" size="xl" color="gray" variant="ghost" @click="isOpen = true" :ui="{ rounded: 'rounded-full' }" />

    <USlideover v-model="isOpen" side="left">
      
      <UCard class="flex flex-col flex-1" :ui="{ body: { base: 'flex-1' }, ring: '', divide: 'divide-y divide-gray-100 dark:divide-gray-800' }">
        <template #header>
          <div class="flex items-center justify-between">
            <SiteTitle />
            <UButton color="gray" variant="ghost" icon="i-heroicons-x-mark-20-solid" class="-my-1" @click="isOpen = false" />
          </div>
        </template>
        <Sidebar />
        <template #footer>
          <UHorizontalNavigation :links="socials" />
          <div class="col-span-12 xl:col-span-6 py-4 text-sm opacity-50">
            <p>Site design / logo &copy; 2013-2024 <ULink class="underline" to="https://codeforpakistan.org">Code for Pakistan</ULink>.</p>
            <p>Content licensed under a <ULink class="underline" to="https://creativecommons.org/licenses/by/4.0/">Creative Commons</ULink> license.</p>
          </div>
        </template>
      </UCard>
    </USlideover>
  </div>
</template>

