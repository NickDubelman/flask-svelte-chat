<script lang="ts">
  import type { Socket } from 'socket.io-client'

  export let socket: Socket

  interface Message {
    id: number
    user: string
    message: string
  }

  let messages: Message[] = []

  $: sortedMessages = messages.sort((a, b) => (a.id > b.id ? -1 : 1))

  socket.on('message', function ({ id, user, message }: Message) {
    // when we receive a message, add it to the list
    messages = [...messages, { id, user, message }]
  })
</script>

{#each sortedMessages as { user, message }}
  <p>{user}: {message}</p>
{/each}

<style>
  p {
    text-align: left;
  }
</style>
