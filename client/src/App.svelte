<script lang="ts">
  import { io } from 'socket.io-client'

  import MessageInput from './components/MessageInput.svelte'
  import MessageList from './components/MessageList.svelte'
  import UserInput from './components/UserInput.svelte'

  const socket = io()

  let user = ''
</script>

<main>
  <UserInput bind:value={user} />
  <MessageInput {socket} {user} />
  <MessageList {socket} />
</main>

<style>
  main {
    text-align: center;
    padding: 1em;
    width: 420px;
    margin: 0 auto;
  }
</style>
