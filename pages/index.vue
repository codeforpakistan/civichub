<script setup lang="ts">

const client = useSupabaseClient()

const { data: activities } = await useAsyncData('activities', async () => {
  const { data } = await client.from('activities').select('id,slug,name,body')
  return data
})
</script>
<template>
  <main>
    <h1 class="text-2xl mb-4">Welcome</h1>
    <div class="grid grid-cols-1 lg:grid-cols-4 gap-4">
      <div v-for="(activity, a) in activities" :key="a">
        <UCard :ui="{ background: 'bg-gray-100', shadow: false }">
          <template #header>
            <h3><ULink class="block" :to="`/activities/${activity.slug}`">{{ activity.name }}</ULink></h3>
          </template>
        </UCard>
      </div>
    </div>
  </main>
</template>