/**
 * Creating a sidebar enables you to:
 - create an ordered group of docs
 - render a sidebar for each doc of that group
 - provide next/previous navigation

 The sidebars can be generated from the filesystem, or explicitly defined here.

 Create as many sidebars as you want.
 */

// @ts-check

/** @type {import('@docusaurus/plugin-content-docs').SidebarsConfig} */
const sidebars = {
  // We create a custom sidebar for the main navigation
  mainSidebar: [
    'intro',
    {
      type: 'category',
      label: 'By Cluster',
      link: {
        type: 'generated-index',
        title: 'Thematic Clusters',
        description: 'The 51 questions are grouped into six thematic clusters for manageable review.',
        slug: '/clusters'
      },
      items: [
        'docs/clusters/Ledger-Foundations-and-Accounting-Parallels/README',
        'docs/clusters/Fidelity-Event-Theory-Auditability/README',
        'docs/clusters/Assets-Liabilities-and-Metrics-in-ESG/README',
        'docs/clusters/Subledgers-Process-Models-and-Supply-Chain/README',
        'docs/clusters/Standards-Data-Flows-and-Confidentiality/README',
        'docs/clusters/Controls-Anti-Greenwashing-and-Technology-Links/README',
      ],
    },
    {
      type: 'category',
      label: 'All Questions',
      link: {
        type: 'generated-index',
        title: 'All Questions',
        description: 'Browse all 51 questions.',
        slug: '/questions'
      },
      items: [
        'docs/questions/Q1',
        'docs/questions/Q2',
        'docs/questions/Q3',
        'docs/questions/Q4',
        'docs/questions/Q5',
        'docs/questions/Q6',
        'docs/questions/Q7',
        'docs/questions/Q8',
        'docs/questions/Q9',
        'docs/questions/Q10',
        'docs/questions/Q11',
        'docs/questions/Q12',
        'docs/questions/Q13',
        'docs/questions/Q14',
        'docs/questions/Q15',
        'docs/questions/Q16',
        'docs/questions/Q17',
        'docs/questions/Q18',
        'docs/questions/Q19',
        'docs/questions/Q20',
        'docs/questions/Q21',
        'docs/questions/Q22',
        'docs/questions/Q23',
        'docs/questions/Q24',
        'docs/questions/Q25',
        'docs/questions/Q26',
        'docs/questions/Q27',
        'docs/questions/Q28',
        'docs/questions/Q29',
        'docs/questions/Q30',
        'docs/questions/Q31',
        'docs/questions/Q32',
        'docs/questions/Q33',
        'docs/questions/Q34',
        'docs/questions/Q35',
        'docs/questions/Q36',
        'docs/questions/Q37',
        'docs/questions/Q38',
        'docs/questions/Q39',
        'docs/questions/Q40',
        'docs/questions/Q41',
        'docs/questions/Q42',
        'docs/questions/Q43',
        'docs/questions/Q44',
        'docs/questions/Q45',
        'docs/questions/Q46',
        'docs/questions/Q47',
        'docs/questions/Q48',
        'docs/questions/Q49',
        'docs/questions/Q50',
        'docs/questions/Q51',
      ],
    },
    'all-in-one',
  ],
};

export default sidebars;
