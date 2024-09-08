<script setup lang="ts">

const client = useSupabaseClient()
const route = useRoute()

const { data: activity } = await useAsyncData('activity', async () => {
  const { data } = await client.from('activities').select('id,name,body,community').eq('slug',route.params.slug).single()
  return data
})

const { data: communities } = await useAsyncData('communities', async () => {
  const { data } = await client.from('communities').select('id,name')
  return data
})

import { object, string, number, type InferType } from 'yup'
import type { FormSubmitEvent } from '#ui/types'

const schema = object({
  community: number().required('Required'),
  name: string().required('Required'),
  body: string().min(8, 'Must be at least 8 characters').required('Required'),
})
type Schema = InferType<typeof schema>

const state = reactive({
  name: activity.value.name,
  body: activity.value.body,
  community: activity.value.community,
})

async function onSubmit (event: FormSubmitEvent<Schema>) {
  const { data, error } = await client.from('activities').update({
    name: state.name, 
    body: state.body, 
    community: state.community 
  }).eq('id', activity.value.id)
  return navigateTo(`/activities/${route.params.slug}`)
}

</script>
<template>
  <UForm :schema="schema" :state="state" @submit="onSubmit">
    <h1 class="text-2xl">Editing activity...</h1>
    <p class="mb-4 opacity-50 italic">Before updating existing content, make sure you have read our <ULink class="underline" to="/policies/content">content policy</ULink>.</p>

    
    <div class="space-y-4">
      <!-- <UAlert v-if="error" color="red" variant="soft" title="Heads up!" /> -->

      <UFormGroup label="Community" name="community">
        <USelectMenu v-model="state.community" :options="communities" placeholder="Select a community" value-attribute="id" option-attribute="name" searchable searchable-placeholder="Search for communities..." size="xl" />
      </UFormGroup>
      <UFormGroup label="Title" name="title">
        <UInput v-model="state.name" placeholder="Title of activity" size="xl" />
      </UFormGroup>
      <UFormGroup label="Description" name="body">
        <UTextarea v-model="state.body" resize placeholder="Description of activity" size="xl" />
      </UFormGroup>
  
      <div class="flex items-center gap-2 pt-4">
        <UButton type="submit" color="green" label="Update" size="xl" />
        <UButton type="button" variant="link" color="gray" label="Cancel" size="xl" @click="$router.back()" />
      </div>

    </div>
  </UForm>
</template>