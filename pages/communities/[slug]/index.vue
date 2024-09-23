<script setup lang="ts">

const client = useSupabaseClient()
const user = useSupabaseUser()
const route = useRoute()

const { data: community } = await useAsyncData('community', async () => {
  const { data } = await client.from('communities').select('name,body,profiles(name,picture)').eq('slug',route.params.slug).single()
  return data
})

const { data: activities } = await useAsyncData('activities', async () => {
  const { data } = await client.from('activities').select('id,slug,name,body')
  return data
})
</script>
<template>
  <main>

    <header class="flex items-center space-x-4">
      <UAvatar :alt="String(community.name).toUpperCase()" size="3xl" />
      <div>
        <h1 class="text-2xl">{{ community.name }}</h1>
        <p class="opacity-50 italic mb-1">{{ community.body || 'There is no description for this community' }}</p>
        <ProfileBadge :user="community?.profiles" />
      </div>
    </header>
    
    <UDivider class="my-8" />

    <div class="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-4 gap-4">
      <div v-for="(activity, a) in activities" :key="a">
        <ActivityCard :activity="activity" />
      </div>
    </div>

  </main>
</template>