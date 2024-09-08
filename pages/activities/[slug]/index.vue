<script setup lang="ts">

const client = useSupabaseClient()
const user = useSupabaseUser()
const route = useRoute()

const { data: activity } = await useAsyncData('activity', async () => {
  const { data } = await client.from('activities').select('id,slug,name,body,author').eq('slug', route.params.slug).single()
  return data
})

const items = [
  [{
    label: 'Edit',
    icon: 'i-heroicons-pencil-square',
    to: `/activities/${activity.value.slug}/edit`
  }, {
    label: 'Delete',
    icon: 'i-heroicons:trash',
    to: `/activities/${activity.value.slug}/delete`
  }]
]

</script>

<template>
  <main>
    <UCard>
      <template #header>
        <UDropdown :items="items" :popper="{ placement: 'bottom-end' }" class="float-right">
          <UButton color="white" label="Options" trailing-icon="i-heroicons-chevron-down-20-solid" />
        </UDropdown>
        <h1 class="text-2xl grow">{{ activity.name }}</h1>
      </template>
      <div>{{ activity.body }}</div>
    </UCard>
  </main>
</template>