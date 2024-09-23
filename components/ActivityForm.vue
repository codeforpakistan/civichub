<script setup lang="ts">

import { object, string, number, type InferType } from 'yup'
import type { FormSubmitEvent } from '#ui/types'

const client = useSupabaseClient()

const props = defineProps({
  communities: { type: Array, required: true },
  activity: { type: Object },
})
const emit = defineEmits(['onSubmit']);

const schema = object({
  community: number().required('Required'),
  name: string().required('Required'),
  body: string().min(8, 'Must be at least 8 characters').required('Required')
})
type Schema = InferType<typeof schema>

const state = reactive({
  name: undefined,
  body: undefined,
  community: undefined,
})

if (props.activity) {
  state.name = props.activity.name
  state.body = props.activity.body
  state.community = props.activity.community_id
}

async function onSubmit (event: FormSubmitEvent<Schema>) {
  emit('onSubmit', state)
}

</script>
<template>
  <UForm :schema="schema" :state="state" @submit="onSubmit" enctype="multipart/form-data">

    <h1 class="text-2xl">{{ !!props.activity ? 'Update' : 'Identify' }} an activity...</h1>
    <p class="mb-4 opacity-50 italic">Before suggesting new content, make sure you have read our <ULink class="underline" to="/policies/content">content policy</ULink>.</p>

    <div class="space-y-4">

      <UFormGroup label="Community" name="community" required>
        <USelectMenu v-model="state.community" :options="props.communities" placeholder="Select a community" value-attribute="id" option-attribute="name" searchable searchable-placeholder="Search for communities..." size="xl" />
      </UFormGroup>
      <UFormGroup label="Title" name="name" required>
        <UInput v-model="state.name" placeholder="Title of activity" size="xl" :disabled="!!props.activity" />
      </UFormGroup>
      <UFormGroup label="Description" name="body" required>
        <UTextarea v-model="state.body" :rows="10" resize placeholder="Description of activity" size="xl" />
      </UFormGroup>

      <div class="flex items-center gap-2">
        <UButton type="submit" label="Save" size="xl" />
        <UButton type="button" variant="link" color="gray" label="Cancel" size="xl" @click="$router.back()" />
      </div>

    </div>

  </UForm>
</template>
