<script setup lang="ts">

const client = useSupabaseClient()
const user = useSupabaseUser()
const route = useRoute()

const { data: activity } = await useAsyncData('activity', async () => {
  const { data } = await client.from('activities').select('id,slug,name,body,author').eq('slug',route.params.slug).single()
  return data
})

async function onSubmit(id) {
  const { error } = await client.from('activities').delete().eq('id', id)
  return navigateTo('/')
}

</script>
<template>
  <UForm @submit="onSubmit(activity.id)">

    <h1 class="text-2xl grow">{{ activity.name }}</h1>
    <p class="mb-4">Are you sure you want to delete this acttivity permanently?</p>

    <div class="flex items-center gap-2 pt-4">
      <UButton type="submit" color="red" label="Delete" size="xl" />
      <UButton type="button" variant="link" color="gray" label="Cancel" size="xl" @click="$router.back()" />
    </div>

  </UForm>
</template>