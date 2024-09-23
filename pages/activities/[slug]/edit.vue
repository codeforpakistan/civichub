<script setup lang="ts">

const client = useSupabaseClient()
const route = useRoute()

const { data: activity } = await useAsyncData('activity', async () => {
  const { data } = await client.from('activities').select('id,name,body,community_id').eq('slug',route.params.slug).single()
  return data
})

const { data: communities } = await useAsyncData('communities', async () => {
  const { data } = await client.from('communities').select('id,name')
  return data
})

async function onSubmit (state: Object) {
  const { data, error } = await client.from('activities').update({
    name: state.name, 
    body: state.body, 
    community: state.community_id
  }).eq('id', activity.value.id)
  return navigateTo(`/activities/${route.params.slug}`)
}

</script>
<template>
  <ActivityForm :communities="communities" :activity="activity" @onSubmit="onSubmit" />
</template>