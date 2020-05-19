#include <stdio.h>

#include <string.h>

 

int main()

{

  int t,n;

  int i,j,l,m,k,count=0,sum=0;

  scanf("%d",&t);

  for(i=0;i<t;i++)

  {

      scanf("%d",&n);

      int arr[n];

      for(j=0;j<n;j++)

      {

         scanf("%d",&arr[j]);

         

   
)
      }

      for(l=0;l<n;l++)

      {

        for(m=l+1;m<n;m++)

        {

            sum=arr[l]+arr[m];

            for(k=0;k<n;k++)

            {

                if(sum==arr[k])

                {

                   

                    count=count+1;

                   

                }

           

            }

            sum=0;

        }

      }if(count==0)

      {

          printf("-1\n");

      }

      else

      {

      printf("%d\n",count);

      count=0;

      }
  }

}