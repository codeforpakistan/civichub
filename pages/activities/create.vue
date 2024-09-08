<script setup lang="ts">

const client = useSupabaseClient()
const user = useSupabaseUser()
const router = useRouter()

const { data: communities } = await useAsyncData('communities', async () => {
  const { data } = await client.from('communities').select('id,name')
  return data
})

import { object, string, number, type InferType } from 'yup'
import type { FormSubmitEvent } from '#ui/types'
import { navigateTo } from 'nuxt/app';

const schema = object({
  community: number().required('Required'),
  name: string().required('Required'),
  body: string().min(8, 'Must be at least 8 characters').required('Required')
})
type Schema = InferType<typeof schema>

const activity = reactive({
  name: undefined,
  body: undefined,
  community: undefined,
  links: undefined,
  images: undefined,
  videos: undefined
})

async function onSubmit (event: FormSubmitEvent<Schema>) {
  const { data } = await client.from('activities').upsert({ 
    name: activity.name, 
    body: activity.body, 
    community: activity.community,
    author: user.id
  }).select()
  return navigateTo(`/activities/${data[0]['slug']}`)
}

</script>
<template>
  <UForm :schema="schema" :state="activity" @submit="onSubmit">
    <h1 class="text-2xl">Identify an activity...</h1>
    <p class="mb-4 opacity-50 italic">Before suggesting new content, make sure you have read our <ULink class="underline" to="/policies/content">content policy</ULink>.</p>

    <div class="space-y-4">
      <UFormGroup label="Community" name="community">
        <USelectMenu v-model="activity.community" :options="communities" placeholder="Select a community" value-attribute="id" option-attribute="name" searchable searchable-placeholder="Search for communities..." size="xl" />
      </UFormGroup>
      <UFormGroup label="Title" name="title">
        <UInput v-model="activity.name" placeholder="Title of activity" size="xl" />
      </UFormGroup>
      <UFormGroup label="Description" name="body">
        <UTextarea v-model="activity.body" resize placeholder="Description of activity" size="xl" />
      </UFormGroup>
      <UFormGroup label="Images" name="images">
        <UInput v-model="activity.images" type="file" size="xl" :padded="true" accept="image/*" multiple />
      </UFormGroup>
      <UFormGroup label="Videos" name="videos">
        <UInput v-model="activity.videos" type="file" size="xl" :padded="true" accept="video/*" multiple />
      </UFormGroup>
      <UFormGroup label="Links" name="links">
        <UTextarea v-model="activity.links" resize placeholder="Social media links" size="xl" />
      </UFormGroup>

      <div class="flex items-center gap-2 pt-4">
        <UButton type="submit" label="Create" size="xl" />
        <UButton type="button" variant="link" color="gray" label="Cancel" size="xl" @click="$router.back()" />
      </div>
    </div>
  </UForm>
</template>