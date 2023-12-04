using System.Collections.Generic;
using System.Threading.Tasks;
using Microsoft.EntityFrameworkCore;
<<<<<<< HEAD:skinet/Infrastructure/Data/GenericRepository.cs
using System.Linq;
using Core.Interfaces;
using Core.Entities;
using Core.Specifications;
=======
using Core.Interfaces;
using Core.Entities;
>>>>>>> 230636b7e1460b19c05f2e368a462a069bde28c5:Infrastructure/Data/GenericRepository.cs

namespace Infrastructure.Data
{
    public class GenericRepository<T> : IGenericRepository<T> where T : BaseEntity
    {
        private readonly StoreContext _context;
        public GenericRepository(StoreContext context) 
        {
            _context = context;
        }
        
        public async Task<T> GetByIdAsync(int id)
        {
            return await _context.Set<T>().FindAsync(id);
        }

        public async Task<IReadOnlyList<T>> ListAllAsync()
        {
            return await _context.Set<T>().ToListAsync();
        }
<<<<<<< HEAD:skinet/Infrastructure/Data/GenericRepository.cs

        public async Task<T> GetEntityWithSpec(ISpecification<T> spec)
        {
            return await ApplySpecification(spec).FirstOrDefaultAsync();
        }

        public async Task<IReadOnlyList<T>> ListAsync(ISpecification<T> spec)
        {
            return await ApplySpecification(spec).ToListAsync();
        }

        private IQueryable<T> ApplySpecification(ISpecification<T> spec)
        {
            return SpecificationEvaluator<T>.GetQuery(_context.Set<T>().AsQueryable(), spec);
        }
=======
>>>>>>> 230636b7e1460b19c05f2e368a462a069bde28c5:Infrastructure/Data/GenericRepository.cs
    }
}