import { useEffect, useState } from 'react'

type HealthResponse = {
  status: string
  database: string
}

type HealthState =
  | { kind: 'loading' }
  | { kind: 'ok'; data: HealthResponse }
  | { kind: 'error'; message: string }

function App() {
  const [health, setHealth] = useState<HealthState>({ kind: 'loading' })

  useEffect(() => {
    fetch('/api/health')
      .then(async (response) => {
        if (!response.ok) {
          throw new Error(`Backend antwortet mit Status ${response.status}`)
        }
        const data = (await response.json()) as HealthResponse
        setHealth({ kind: 'ok', data })
      })
      .catch(() => {
        setHealth({
          kind: 'error',
          message: 'Backend nicht erreichbar. Läuft der Server auf Port 8000?',
        })
      })
  }, [])

  return (
    <main className="page">
      <h1>AI Running Coach</h1>
      <p className="subtitle">Train smarter, not just harder.</p>

      <section className="card">
        <h2>Systemstatus</h2>
        {health.kind === 'loading' && <p>Verbinde mit dem Backend …</p>}
        {health.kind === 'ok' && (
          <dl>
            <dt>Backend</dt>
            <dd className="ok">{health.data.status}</dd>
            <dt>Datenbank</dt>
            <dd className="ok">{health.data.database}</dd>
          </dl>
        )}
        {health.kind === 'error' && <p className="error">{health.message}</p>}
      </section>
    </main>
  )
}

export default App
