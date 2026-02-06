import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import {
  DataTableModule,
  PaginationModule,
  ButtonModule,
  SearchModule,
  TagsModule,
  TableWidthConfig
} from 'ng-devui';

export interface SourceType {
  id: number;
  title: string;
  priority: string;
  status: string;
  assignee: string;
}

@Component({
  selector: 'app-table-page',
  standalone: true,
  imports: [
    CommonModule,
    FormsModule,
    DataTableModule,
    PaginationModule,
    ButtonModule,
    SearchModule,
    TagsModule
  ],
  templateUrl: './table-page.html',
  styleUrl: './table-page.scss',
})
export class TablePage {
  basicDataSource: SourceType[] = [
    { id: 1, title: 'Fix bug in table', priority: 'High', status: 'Done', assignee: 'Mark' },
    { id: 2, title: 'Add new feature', priority: 'Medium', status: 'In Progress', assignee: 'Jacob' },
    { id: 3, title: 'Update documentation', priority: 'Low', status: 'Done', assignee: 'Larry' },
    { id: 4, title: 'Refactor code', priority: 'High', status: 'In Progress', assignee: 'John' },
    { id: 5, title: 'Write tests', priority: 'Medium', status: 'Waiting', assignee: 'Doe' },
    { id: 6, title: 'Deploy to staging', priority: 'High', status: 'Done', assignee: 'Smith' },
    { id: 7, title: 'Review PR', priority: 'Low', status: 'Done', assignee: 'Jane' },
    { id: 8, title: 'Design new UI', priority: 'Medium', status: 'In Progress', assignee: 'Alice' },
    { id: 9, title: 'Fix CSS issues', priority: 'Low', status: 'Waiting', assignee: 'Bob' },
    { id: 10, title: 'Optimize performance', priority: 'High', status: 'In Progress', assignee: 'Charlie' },
    { id: 11, title: 'Update dependencies', priority: 'Low', status: 'Done', assignee: 'David' },
    { id: 12, title: 'Fix login bug', priority: 'High', status: 'Waiting', assignee: 'Eve' },
  ];

  tableWidthConfig: TableWidthConfig[] = [
    { field: 'id', width: '100px' },
    { field: 'title', width: '300px' },
    { field: 'priority', width: '150px' },
    { field: 'status', width: '150px' },
    { field: 'assignee', width: '150px' },
    { field: 'actions', width: '150px' }
  ];

  pager = {
    total: 12,
    pageIndex: 1,
    pageSize: 10
  };

  onSearch(term: string) {
    console.log('Search:', term);
  }

  onPageChange(pageIndex: number) {
    console.log('Page changed:', pageIndex);
  }
}
