<script setup lang="ts">

const client = useSupabaseClient()

const { data: activities } = await useAsyncData('activities', async () => {
  const { data } = await client.from('activities').select('id,slug,name,body')
  return data
})
</script>
<template>
  <h1 class="text-2xl mb-4">Welcome</h1>
  <div class="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-4 gap-4">
    <div v-for="(activity, a) in activities" :key="a">
      <ActivityCard :activity="activity" />
    </div>
  </div>
</template>