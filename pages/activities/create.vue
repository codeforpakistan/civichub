<script setup lang="ts">

const client = useSupabaseClient()
const user = useSupabaseUser()

const { data: communities } = await useAsyncData('communities', async () => {
  const { data } = await client.from('communities').select('id,name')
  return data
})

import { navigateTo } from 'nuxt/app';

async function onSubmit (state: Object) {
  const { data } = await client.from('activities').upsert({ 
    name: state.name, 
    body: state.body, 
    community_id: state.community,
    profile_id: user.id
  }).select().single()
  return navigateTo(`/activities/${data.slug}`)
}

</script>
<template>
  <ActivityForm :communities="communities" @onSubmit="onSubmit" />
</template>