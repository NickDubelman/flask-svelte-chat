<script lang="ts">
  import { io } from 'socket.io-client'
  import MessageInput from './components/MessageInput.svelte'

  const socket = io()
  socket.on('connect', function () {
    socket.emit('message', 'ping')
  })

  socket.on('message', function (data) {
    console.log(data)
  })
</script>

<main>
  <MessageInput />
</main>

<style>
  main {
    text-align: center;
    padding: 1em;
    max-width: none;
    margin: 0 auto;
  }
</style>
