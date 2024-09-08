<script setup lang="ts">

const client = useSupabaseClient()

const { data: communities } = await useAsyncData('communities', async () => {
  const { data } = await client.from('communities').select('id,slug,name,body')
  return data
})
</script>
<template>
  <main>
    <h1 class="text-2xl mb-4">Communities</h1>
    <div class="grid grid-cols-1 lg:grid-cols-4 gap-4">
      <div v-for="(hub, h) in communities" :key="h">
        <UCard>
          <template #header>
            <h3><ULink :to="`/communities/${hub.slug}`">{{ hub.name }}</ULink></h3>
          </template>
        </UCard>
      </div>
    </div>
  </main>
</template>