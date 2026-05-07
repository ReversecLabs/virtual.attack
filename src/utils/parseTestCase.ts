export interface TestCase {
  slug: string;
  title: string;
  component: string;
  mitreId: string;
  tactic: string;
  description: string;
  threatActors: string[];
  logSources: string[];
  references: string[];
  author: string;
}

export function parseTestCase(body: string, slug: string): TestCase {
  const lines = body.split('\n');
  const sections: Record<string, string[]> = {};
  let currentSection = '';
  let title = '';

  for (const line of lines) {
    if (line.startsWith('# ') && !title) {
      title = line.slice(2).trim();
    } else if (line.startsWith('## ')) {
      currentSection = line.slice(3).trim();
      sections[currentSection] = [];
    } else if (currentSection) {
      sections[currentSection].push(line);
    }
  }

  const getSection = (name: string) =>
    (sections[name] ?? []).join('\n').trim();

  const component = getSection('Component').replace(/\*\*/g, '').trim();

  const mitreRaw = getSection('MITRE ATT&CK');
  const idMatch = mitreRaw.match(/\*\*ID:\*\*\s*(.+)/);
  const tacticMatch = mitreRaw.match(/\*\*Tactic:\*\*\s*(.+)/);

  const parseList = (name: string): string[] =>
    (sections[name] ?? [])
      .map(l => l.replace(/^[-*]\s*/, '').trim())
      .filter(l => l && l !== '_None_' && l.toLowerCase() !== 'none');

  return {
    slug,
    title: title || slug.split('/').pop()?.replace(/-/g, ' ') || slug,
    component: component || 'Unknown',
    mitreId: idMatch ? idMatch[1].trim() : '',
    tactic: tacticMatch ? tacticMatch[1].trim() : '',
    description: getSection('Description'),
    threatActors: parseList('Threat Actors'),
    logSources: parseList('Log Sources'),
    references: parseList('References'),
    author: getSection('Author'),
  };
}
