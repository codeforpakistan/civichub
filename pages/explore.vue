<script setup lang="ts">

const client = useSupabaseClient()

const { data: communities } = await useAsyncData('communities', async () => {
  const { data } = await client.from('communities').select('id,slug,name,body')
  return data
})
</script>
<template>
  <h1 class="text-2xl mb-4">Communities</h1>
  <div class="grid grid-cols-1 lg:grid-cols-4 gap-4">
    <div v-for="(community, c) in communities" :key="c">
      <CommunityCard :community="community" />
    </div>
  </div>
</template>