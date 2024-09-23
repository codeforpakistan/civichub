<script setup lang="ts">

const client = useSupabaseClient()
const user = useSupabaseUser()
const route = useRoute()

const { data: activity } = await useAsyncData('activity', async () => {
  const { data } = await client.from('activities').select('id,slug,name,body,images,videos,links,created_at,communities(name,slug),profiles(id,name,picture)').eq('slug', route.params.slug).single()
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
  <UContainer :ui="{ constrained: 'max-w-screen-md' }">
    <UCard>
      <template #header>
        <UDropdown v-if="activity?.profiles.id == user.id" :items="items" :popper="{ placement: 'bottom-end' }" class="float-right">
          <UButton color="gray" variant="ghost">
            <UIcon name="i-ic:outline-more-vert" class="w-5 h-5" />
          </UButton>
        </UDropdown>
        <header class="flex items-center gap-2 mb-2">
          <UAvatar :alt="String(activity.communities.name).toUpperCase()" size="xs" />
          <NuxtLink class="hover:underline" :to="`/communities/${activity.communities.name}`">{{ activity.communities.name }}</NuxtLink>
          <span class="text-xs opacity-50">&bull;</span>
          <span class="text-xs opacity-50">{{ timeSince(activity.created_at) }}</span>
          <ProfileBadge :user="activity?.profiles" />
        </header>
        <h1 class="text-2xl grow">{{ activity.name }}</h1>
      </template>
      <div>{{ activity.body }}</div>
    </UCard>
  </UContainer>
</template>