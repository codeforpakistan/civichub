<script setup lang="ts">

const client = useSupabaseClient()
const user = useSupabaseUser()
const route = useRoute()

const { data: community } = await useAsyncData('community', async () => {
  const { data } = await client.from('communities').select('name,body').eq('slug',route.params.slug).single()
  return data
})

const { data: activities } = await useAsyncData('activities', async () => {
  const { data } = await client.from('activities').select('id,slug,name,body')
  return data
})
</script>
<template>
  <main>
    <h1 class="text-2xl">{{ community.name }}</h1>
    <p class="mb-4 opacity-50 italic">{{ community.body || 'There is no description for this community' }}</p>

    <div class="grid grid-cols-4 gap-4">
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